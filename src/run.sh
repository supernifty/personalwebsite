
python ./src/generate_html.py --template index.template > index.html
rsync -avzP -e "ssh -i ~/.ssh/vultr" index.html assets favicon peter@cog.supernifty.org:/var/www/petergeorgeson/
