import sys, argparse
import gensim
import os
#Model tester

parser = argparse.ArgumentParser('for testing word2vec models')
parser.add_argument('--filename', required=True, action='store', dest='filename')
args = parser.parse_args()

#fetching model name
model_name = args.filename
if not os.path.isfile(model_name):
    raise Exception('File ' + model_name + ' not found.')
    quit()

model = gensim.models.Word2Vec.load(model_name)
print('Model loaded')
user_input_expression = 'foo'
while user_input_expression.lower()  != 'x':
    print('Please write expression (x to exit):')
    user_input_expression = input()
    word = ''
    result_matrix = None
    first_is_set = False
    previous_operator = lambda _,_2: []
    try:
        for char in user_input_expression:
            if char == '+':
                word = word.strip()
                if first_is_set is False:
                    first_is_set = True
                    result_matrix = model.wv[word]
                else:
                    result_matrix = previous_operator(result_matrix, model.wv[word])
                
                previous_operator = lambda m1, m2: m1 + m2
                word = ''
            elif char == '-':
                word = word.strip()
                if first_is_set is False:
                    first_is_set = True
                    result_matrix = model.wv[word]
                else:
                    result_matrix = previous_operator(result_matrix, model.wv[word])

                previous_operator = lambda m1, m2: m1 - m2
                word = ''
            elif char == '*':
                word = word.strip()
                if first_is_set is False:
                    first_is_set = True
                    result_matrix = model.wv[word]
                else:
                    result_matrix = previous_operator(result_matrix, model.wv[word])

                previous_operator = lambda m1, m2: m1 * m2
                word = ''
            elif char == '/':
                word = word.strip()
                if first_is_set is False:
                    first_is_set = True
                    result_matrix = model.wv[word]
                else:
                    result_matrix = previous_operator(result_matrix, model.wv[word])

                previous_operator = lambda m1, m2: m1 / m2
                word = ''
            else:
                word += char
                pass

        word = word if first_is_set else user_input_expression
        result_matrix = previous_operator(result_matrix, model.wv[word]) if first_is_set else model.wv[word]
        result = model.wv.similar_by_vector(result_matrix)
        print(user_input_expression + ' =>\n' + str(result))
    except:
        print("word not found...")

print('done...')
quit()