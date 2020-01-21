import datetime



class Message(object):

    def __init__(self, from_:str=None, to:str=None, text:str=None, timestamp=None):
        self.from_ , self.to, self.text = from_, to, text
        self.date = datetime.datetime.fromtimestamp(timestamp) if timestamp != None else datetime.datetime

    def toJson(self) -> dict:
        return {
            'from': self.from_,
            'to': self.to,
            'text': self.text,
            'date': self.date.timestamp()
        }

    @staticmethod
    def fromJson(data:dict) -> Message:
        return Message(
            from_=data['from'],
            to=data['to'],
            text=data['text'],
            timestamp=data['date']
        )


