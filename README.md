# WSUtil
Utilitaire pour un serveur websocket en python


Manifest
- Server
- Message

pour envoyer un message d'un serveur client il est important de respecter la structure du message

from: string
to: string
text: string
date: timestamp


message en json
`
{
  "from": "foo",
  "to": "bar",
  "text": "foobar",
  "date": 123553789
}

`
