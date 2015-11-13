import string

class NewsStory(object):
    def __init__(self, guid, title, subject, summary, link):
        self.myguid = guid
        self.mytitle = title
        self.mysubject = subject
        self.mysummary = summary
        self.mylink = link
    def getGuid(self):
        return self.myguid
    def getTitle(self):
        return self.mytitle
    def getSubject(self) :
        return self.mysubject
    def getSummary(self) :
        return self.mysummary
    def getLink(self) :
        return self.mylink

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError


class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word
    def isWordIn(self, text):
        s = text.lower()
        s = s.replace("'s",'')
        for i in string.punctuation:
            s=s.replace(i,' ')
        s2 = s.split(' ')
        return self.word.lower() in s2
    
        
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())

class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())

class NotTrigger(Trigger) :
    def __init__(self, trigger):
        self.trigger = trigger
    def evaluate(self, story):
        return not self.trigger.evaluate(story)

class AndTrigger(Trigger) :
    def __init__(self, trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, story):
        return self.trigger1.evaluate(story) and self.trigger2.evaluate(story)

class OrTrigger(Trigger) :
    def __init__(self, trigger1,trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, story):
        return self.trigger1.evaluate(story) or self.trigger2.evaluate(story)

class PhraseTrigger(Trigger) :
    def __init__(self, shorttext):
        self.shorttext = shorttext
    def evaluate(self, story) :
        return (self.shorttext in story.getTitle()) or (self.shorttext in story.getSummary()) or (self.shorttext in story.getSubject())

story = NewsStory('foo','myTitle','mySubject','some long summary','www.example.com')
tTriger = TitleTrigger('Mytitle')
sub = SubjectTrigger('mysubject')
print(sub.evaluate(story))
ntigger = NotTrigger(sub)
print(ntigger.evaluate(story))
atrigger = AndTrigger(tTriger,sub)
print(atrigger.evaluate(story))
ortrigger = AndTrigger(tTriger,sub)
print(ortrigger.evaluate(story))
ptrigger = PhraseTrigger("mySubject")
print(ptrigger.evaluate(story))
