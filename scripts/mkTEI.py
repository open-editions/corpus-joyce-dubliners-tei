# This is just to do as much as I can to automatically convert Gabler's originals to TEI.
# This will get us started, and hopefully cut out some of the grunt-work.

# I've already done "The Sisters" and "Ivy Day" manually. 
filenames = [fn + '.xml' for fn in 
            ['02_enc', '03_ara', '04_eve', '05_aft',
             '06_two', '07_boa', '08_lit', '09_cou', '10_cla',
             '11_pai', '13_mot', '14_gra', '15_dea']]

# Add divs
stories = [open(fn).read() for fn in filenames]

for fn, story in zip(filenames, stories):
    lines = story.split('\n')
    lines[0] = lines[0].replace('<emph>', '<head rend="italics">').replace('</emph>', '</head>')
    story = '\n'.join(lines)
    # Don't know where these pipe characters come from, but let's ditch them.
    story = story.replace('|', '')
    # Replace double hyphens with dialogue dashes
    story = story.replace('<said who="">--</said>', '<said who="">―</said>')
    beginning = '<div n="{}" type="story">'.format(fn[:2])
    end = '</div> <!-- End of story -->'
    story = beginning + story + end
    open(fn, 'w').write(story)
