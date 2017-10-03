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

def file_to_string(path, encoding='utf-8'):
	with open(path, 'r', encoding=encoding) as fp:
		ret = fp.read()
	return ret

content = file_to_string('test.txt')
token_list = TokenList(content, stopwords=["'", ".", ",", "!", "\ufeff", "“", "”", '"', "[", "]", "=", "…", "(", ")", "{", "}", ":", ":", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
dic = token_list.to_dic_by_count()
sorted_list = sorted(dic, key=lambda x:dic[x])
for s in sorted_list:
	if dic[s] <= 1: continue
	print(s, dic[s])