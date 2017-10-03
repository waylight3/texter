class TokenList:
	def __init__(self, content, delimiter=None, stopwords=[]):
		for stopword in stopwords:
			content = content.replace(stopword, delimiter if delimiter else ' ')
		if delimiter:
			tokens = content.split()
		else:
			tokens = content.split(delimiter)
		self.tokens = tokens

	def to_dic_by_index(self):
		dic = {}
		for i in range(len(self.tokens)):
			token = self.tokens[i]
			if token in dic:
				dic[token].append(i)
			else:
				dic[token] = [i]
		return dic

	def to_dic_by_count(self):
		dic = {}
		for token in self.tokens:
			if token in dic:
				dic[token] += 1
			else:
				dic[token] = 1
		return dic

	def print(self):
		for token in self.tokens:
			print(token)

content = "Hello, I'm AA and this is my friend BB. Nice to meet you!"
token_list = TokenList(content, stopwords=["'", ".", ",", "!"])
print(token_list.to_dic_by_count())
print(token_list.to_dic_by_index())