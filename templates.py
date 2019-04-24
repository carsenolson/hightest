from string import Template


# There is no support for static files, 
# so you have to write your styles and js stuff right here :) 

nav = Template(
        '''
            <!DOCTYPE html>
                <head> 
                    <meta charset="utf-8">   <style>
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

# These templates created for test_server.py!

students_name_form = '''
                    <form method="post" id="student_form">
                        <input type="text" name="student_name" placeholder="your name"> 
                        <input type="text" name="student_group" placeholder="your group"> 
                        <input type="submit">
                    </form>
                    <select name="test_name" form="student_form">
                    '''
test_option = Template('''<option value="$test_name">$test_name</option>''')
end_students_name_form = '''</select>'''

start_form = '''<form method="post">'''
question_title_h3 = Template('''<h3>$question_title</h3>''')
question_answer = Template('''<p>$question_answer</p>''')
input_answer = '''<input type="texd" name="answers" placeholder="enter your answers (0;2)">'''
end_form = '''
                    <input type="submit" value="okay"> 
                </form>  
            '''
