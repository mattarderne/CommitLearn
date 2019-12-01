from feedgen.feed import FeedGenerator
import yaml

DOMAIN = 'http://rdrn.dev/CommitLearn'
class Podcast:

    episode_count = 0
    def __init__(self, name, category,title, subtitle):
    self.name = name
    self.category = []
    self.title = title
    self.subtitle = subtitle

    def links(self):
        self.id = DOMAIN + self.name

    def episode():

class Episode(Podcast): # define child class
   def __init__(self):
      print "Calling child constructor"
        Podcast.episode_count += 1

   def childMethod(self):
      print 'Calling child method'

print(p1.name)
print(p1.age) 


def gen_podcast(podcast_file):
    fg = FeedGenerator()
    fg.load_extension('podcast')
    fg.language('en')

    fg.podcast.itunes_category('Technology', 'Podcasting')
    fg.title('Some Testfeed')
    fg.subtitle('This is a cool feed!')
    fg.id(f'http://rdrn.dev/CommitLearn/{name}.xml')
    fg.logo('http://ex.com/logo.jpg')
    fg.link( href='http://example.com', rel='alternate' )
    fg.link( href='http://larskiesow.de/test.atom', rel='self' )
    fg.rss_file(f'static/{name}.xml') # Write the RSS feed to a file
    rssfeed  = fg.rss_str(pretty=True) # Get the RSS feed as string
    return rssfeed

def add_entry(podcast, entry):
    fe = fg.add_entry()
    fe.id('http://lernfunk.de/media/654321/1/file.mp3')
    fe.description('Enjoy our first episode.')
    fe.enclosure('http://lernfunk.de/media/654321/1/file.mp3', 0, 'audio/mpeg')
    fg.author( {'name':'John Doe','email':'john@example.de'} )
    fg.rss_file(f'static/{name}.xml')
    rssfeed  = fg.rss_str(pretty=True) # Get the RSS feed as string
    return rssfeed

def create_podcast(file):
    podcast_list = yaml.full_load(file)
    for item, doc in podcast_list.items():
        gen_podcast()

with open(r'content/podcasts.yaml') as file:
    create_podcast(file)