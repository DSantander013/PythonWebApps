from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'heroes.html'


class HulkView(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'id': 'Bruce Banner',
            'power1': 'super strength',
            'power2': 'huge',
            'power3': 'gets tronger when angry',
            'weakness1': 'radiation',
            'weakness2': 'not too bright',
            'weakness3': 'fights with alter ego',
            'body': 'My name is Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }


class IronManView(TemplateView):
    template_name = "hero.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Iron Man',
            'id': 'Tony Stark',
            'power1': 'intelligent',
            'power2': 'nanotech',
            'power3': 'armor',
            'weakness1': 'too cocky',
            'weakness2': 'big ego',
            'weakness3': 'has something in his chest',
            'body': 'My name is Tony Stark, but I am Iron Man',
            'image': '/static/images/iron_man.jpg'
        }


class SpiderMan(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Spider Man',
            'id': 'Peter Parker',
            'power1': 'super strength',
            'power2': 'shoot webs',
            'power3': 'climb walls',
            'weakness1': 'a pesticide only works on him',
            'weakness2': 'family',
            'weakness3': 'too naive',
            'body': 'My name is Peter Parker',
            'image': '/static/images/spiderman1.jpg'
        }
    
class CaptainAmerica(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Captain America',
            'id': 'Steve Rogers',
            'power1': 'enhanced strength',
            'power2': 'enhanced speed',
            'power3': 'good with shield',
            'weakness1': 'human',
            'weakness2': 'moral code',
            'weakness3': 'friends',
            'body': 'My name is Steve Rodgers',
            'image': '/static/images/captainamerica.jpg'
        }

class TheFlash(TemplateView):
    template_name = 'hero.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'The Flash',
            'id': 'Barry Allen',
            'power1': 'Super Speed',
            'power2': 'Super healing',
            'power3': 'time travel',
            'weakness1': 'cold',
            'weakness2': 'love for others',
            'weakness3': 'family',
            'body': 'My name is Barry Allen',
            'image': '/static/images/theflash.jpg'
        }