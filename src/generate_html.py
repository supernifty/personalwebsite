#!/usr/bin/env python
'''
  update html template
'''

import argparse
import json
import logging
import sys

TEMPLATES = {
  'publications': {
    'filename': 'data/publications.json',
    'template': '''<div><p><b><i>{{ title }}</i></b>. {{ author }}<i>{{ journal }}</i>. {{ year }}.</p><p class="text-end"><a href="{{ url }}" class="text-secondary" target="_blank" rel="noopener noreferrer">[{{ doi }}]</a></p></div>'''
  },
  'presentations': {
    'filename': 'data/presentations.json',
    'template': '''<li><span><b>{{ title }}</b><br><i>{{ where }}</i> ({{ when }}). {{ type }}.<br><br></span></li>'''
  },
  'funding': {
    'filename': 'data/funding.json',
    'template': '''<li><span><b>{{ funder }} ({{ when }})</b> - {{ amount }}<br><a href="{{ link }}" target="_blank" rel="noopener noreferrer">{{ title }}</a><br/><br/></span></li>'''
  },
  'supervision': {
    'filename': 'data/supervision.json',
    'template': '''<li><span><b>{{ who }} ({{ when }})</b><br/>{{ what }}<br/><br/></span></li>'''
  },
  'teaching': {
    'filename': 'data/teaching.json',
    'template': '''<li><span><b>{{ role }} ({{ when }})</b>:<br/><a href="{{ courseLink }}" target="_blank" rel="noopener noreferrer">{{ course }}</a> at <a href="{{ institutionLink }}" target="_blank" rel="noopener noreferrer">{{ institutionName }}</a> {{ note }}<br/><br/></span></li>'''
  },
  'projects': {
    'filename': 'data/projects.json',
    'template': '''<div class="container text-left"><div class="shadow p-3 mb-5 bg-body rounded"><div class="row"><div class="col-md-auto"><span class="mt-5" style="box-sizing: border-box; display: inline-block; overflow: hidden; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; position: relative; max-width: 100%;"><span style="box-sizing: border-box; display: block; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; max-width: 100%;"><img alt="" aria-hidden="true" src="data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27260%27%20height=%27260%27/%3e" style="display: block; max-width: 100%; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px;"></span><img draggable="false" alt="{{ title }}" src="{{ img }}" decoding="async" data-nimg="intrinsic" class="rounded-full select-none transition-all pointer-events-none rounded-md" style="position: absolute; inset: 0px; box-sizing: border-box; padding: 0px; border: none; margin: auto; display: block; width: 0px; height: 0px; min-width: 100%; max-width: 100%; min-height: 100%; max-height: 100%; border-radius:50%"></span></div><div class="col col-lg-6"><h3>{{ title }}</h3><p>{{ description }}<br/><br/><a href="{{ url }}" target="_blank" rel="noopener noreferrer">Learn more!</a></p></div></div></div></div>'''
  },
  'misc': {
    'filename': 'data/misc.json',
    'template': '''<div class="container text-left"><div class="shadow p-3 mb-5 bg-body rounded"><div class="row"><div class="col-md-auto"><span class="mt-5" style="box-sizing: border-box; display: inline-block; overflow: hidden; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; position: relative; max-width: 100%;"><span style="box-sizing: border-box; display: block; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px; max-width: 100%;"><img alt="" aria-hidden="true" src="data:image/svg+xml,%3csvg%20xmlns=%27http://www.w3.org/2000/svg%27%20version=%271.1%27%20width=%27260%27%20height=%27260%27/%3e" style="display: block; max-width: 100%; width: initial; height: initial; background: none; opacity: 1; border: 0px; margin: 0px; padding: 0px;"></span><img draggable="false" alt="{{ title }}" src="{{ img }}" decoding="async" data-nimg="intrinsic" class="rounded-full select-none transition-all pointer-events-none rounded-md" style="position: absolute; inset: 0px; box-sizing: border-box; padding: 0px; border: none; margin: auto; display: block; width: 0px; height: 0px; min-width: 100%; max-width: 100%; min-height: 100%; max-height: 100%; border-radius:50%"></span>
    </div><div class="col col-lg-6"><h3>{{ title }}</h3><p>{{ description }}<br/><br/><a href="{{ url }}" target="_blank" rel="noopener noreferrer">Learn more!</a></p></div></div></div></div>'''
  }
}
#    {{ misc }}
#    'template': '''<div class="container text-left"><div class="shadow p-3 mb-5 bg-body rounded"><div class="row"><div class="col-md-auto"><img class="" width="200px" draggable="false" alt="{{ title }}" src="{{ img }}"/></div><div class="col col-lg-6"><h3>{{ title }}</h3><p>{{ description }}<br/><br/><a href="{{ url }}" target="_blank" rel="noopener noreferrer">Learn more!</a></p></div></div></div></div>'''


def main(template, ofh):
  logging.info('starting...')

  i = ''.join(open(template, 'rt').readlines())
  for t in TEMPLATES:
    pubs = json.load(open(TEMPLATES[t]['filename'], 'rt'))
    html = []
    for pub in pubs:
      item = TEMPLATES[t]['template']
      for k in pub:
        item = item.replace('{{{{ {} }}}}'.format(k), pub[k])
      html.append(item)
    i = i.replace('{{{{ {} }}}}'.format(t), '\n'.join(html))

  ofh.write(i)
  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Assess MSI')
  parser.add_argument('--template', help='more logging')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  main(args.template, sys.stdout)
