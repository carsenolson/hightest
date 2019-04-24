from string import Template


# There is no support for static files, 
# so you have to write your styles and js stuff right here :) 

nav = Template(
        '''
            <!DOCTYPE html>
                <head> 
                    <meta charset="utf-8">   
                    <style>
                        body {
                            background: #eaeaea;
                            margin: 0;
                            padding: 0;
                        }
                    </style>
                </head>    
                    <a href="/">Go to home</a><hr> 
                    <h3>$page_name</h3>  
        '''
        )
test_list = Template('''<a href="/$test_name/">$test_name</a><br>''')

question_list = Template(
            ''' 
            <div class="question">
                <a href="/$test_name/$question_index">$question_index -> $question_title...</a>
                <a href="/$test_name/$question_index/delete">delete</a>
            </div>
            '''
        )

question_form = Template(
            '''
                <form method="post"> 
                    <input type="text" name="question_title" placeholder="question title" value="$question_title"><br>
                    <input type="text" name="answers" placeholder="answers (answer;answer)" value="$answers"><br> 
                    <input type="text" name="true_answers" placeholder="true answers (0;2) " value="$true_answers"><br> 
                    <input type="submit" value="add"> 
                </form> 
            ''' 
        )

empty_question_form = '''

                <form  method="post"> 
                    <input type="text" name="question_title" placeholder="question title" ><br>
                    <input type="text" name="answers" placeholder="answers (answer;answer)" ><br> 
                    <input type="text" name="true_answers" placeholder="true answers (0;2) " ><br> 
                    <input type="submit" value="add"> 
                </form> 

            '''
add_new_question_link = Template('''<a href="/$test_name/$question_index">add new question</a>''')

new_test_form =  '''
                <form method="POST"> 
                    <input type="text" name="test_name" placeholder="test name">
                    <input type="submit" value="create test"> 
                </form> 
            '''

add_question_link = Template('''<a href="/$test_name/$questoin_index">  </a> ''')  
