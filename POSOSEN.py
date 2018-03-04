import json
data = None
topics = None
inp='''{
 "entities": [
  {
   "name": "Trump",
   "salience": 0.45490643,
   "sentiment": {
    "magnitude": 0.5,
    "score": -0.1
   }
  },
  {
   "name": "Jeff Sessions",
   "salience": 0.13912244,
   "sentiment": {
    "magnitude": 0.1,
    "score": 0
   }
  },
  {
   "name": "actions",
   "salience": 0.11479895,
   "sentiment": {
    "magnitude": 0.1,
    "score": 0.1
   }
  },
  {
   "name": "investigations",
   "salience": 0.07787295,
   "sentiment": {
    "magnitude": 0,
    "score": 0
   }
  },
  {
   "name": "Clinton",
   "salience": 0.04593142,
   "sentiment": {
    "magnitude": 0,
    "score": 0
   }
  },
  {
   "name": "Twitter",
   "salience": 0.03692253,
   "sentiment": {
    "magnitude": 0,
    "score": 0
   }
  },
  {
   "name": "email server",
   "salience": 0.0323256,
   "sentiment": {
    "magnitude": 0.1,
    "score": 0.1
   }
  },
  {
   "name": "Clinton",
   "salience": 0.03160303,
   "sentiment": {
    "magnitude": 0.4,
    "score": 0.4
   }
  },
  {
   "name": "steps",
   "salience": 0.020585226,
   "sentiment": {
    "magnitude": 0.9,
    "score": 0.9
   }
  }
 ]
}'''

TRAINSET = {
	'red':{
		'Trump':[
			{'fox': {'magnitude': 2.0, 'score': 0.8}},
			{'breinbart': {'magnitude': 2.0, 'score': 1.2}}
		]
	},
	'blue':{
		'Trump':[
			{'cnn': {'magnitude': 2.0, 'score': -0.8}},
			{'shareblue': {'magnitude': 2.0, 'score': -4.8}}
		]
	}
}

def load(input):
	return json.loads(input.replace('\n', ''))

def strip(input):
	return input['entities']

def getTopics(input, top=1):
	xs = strip(input).copy()
	output = []
	for i in range(top):
		x = getTop(xs)
		output += [x]
		xs.remove(x)
	return output

def getTop(input):
	output = {'salience':-1.0}
	for x in input:
		if x['salience'] > output['salience']:
			output = x
	return output

#C-C-C-COMBO BREAKER
#Political Sentiment Cencus and Analysis
def PSCA(terms):
	output={}
	for term in terms:
		for side, dataset in TRAINSET.items():
			for source in dataset[term['name']]:
				for sentiment in source.values():
					output.update({side:abs(sentiment['score']-term['sentiment']['score'])})
	return output

def init():
	global data
	global topics
	data = load(inp)
	topics = getTopics(data)
