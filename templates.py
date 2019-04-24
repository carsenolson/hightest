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
                            background: #fff;
                            margin: 0;
                            padding: 0;
                        }
                        a {
                            text-decoration: none;
                            margin: 0px 10px; 
                            padding: 10px; 
                        }
                        a:hover {
                            text-decoration: underline;
                        }
                        .question {
                            width:280px;
                            height:40px;
                            background: #eee; 
                            border: 1px solid #ccc; 
                        }
                        
                        input[type=text] {
                            width: 50%;
                            padding: 12px 20px;
                            margin: 8px 0;
                            box-sizing: border-box;
                        } 
                        input[type=button], input[type=submit], input[type=reset] {
                            background-color: #4CAF50;
                            border: none;
                            color: white;
                            padding: 16px 32px;
                            text-decoration: none;
                            margin: 4px 2px;
                            cursor: pointer;
                        }     
                        h2 {
                            margin: 10px;
                        }
                    </style>
                </head>    
                    <a href="/"><h1>Go to home</h1></a><hr> 
                    <h3>$page_name</h3>  
        '''
        )
test_list = Template('''<a href="/$test_name/"><h2>$test_name</h2></a><br>''')

question_list = Template(
            ''' 
            <div class="question">
                <a href="/$test_name/$question_index">$question_index -> $question_title...</a>
                <a href="/$test_name/$question_index/delete" style="color:red">delete</a>
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

nav1 = '''
        <!DOCTYPE html>
        <head>
            <meta charset="utf-8">
            <style>
                        body {
                            background: #fff;
                            margin: 0;
                            padding: 0;
                        }
                        a {
                            text-decoration: none;
                            margin: 0px 10px; 
                            padding: 10px; 
                        }
                        a:hover {
                            text-decoration: underline;
                        }
                        .question {
                            width:280px;
                            height:40px;
                            background: #eee; 
                            border: 1px solid #ccc; 
                        }
                        select {
                            width: 50%;
                            padding: 16px 20px;
                            border: none;
                            border-radius: 4px;
                            background-color: #f1f1f1;
                        } 
                        input[type=text] {
                            width: 50%;
                            padding: 12px 20px;
                            margin: 8px 0;
                            box-sizing: border-box;
                        } 
                        input[type=button], input[type=submit], input[type=reset] {
                            background-color: #4CAF50;
                            border: none;
                            color: white;
                            padding: 16px 32px;
                            text-decoration: none;
                            margin: 4px 2px;
                            cursor: pointer;
                        }     
                        h2 {
                            margin: 10px;
                        }
                    </style>
        </head>
        '''

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


