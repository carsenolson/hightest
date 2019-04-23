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
                    <h3>$page_name</h3>  
        '''
        )
test_list = Template('''<a href="/$test_name/">$test_name</a><br>''')

question_list = Template(
            ''' 
            <div class="question">
                <a href="/$test_name/$question_index">$question_index -> $question_title...</a>
            </div>
            '''
        )

selection_question_form = Template(
            '''
            <div>
                <form action="/$test_name/questoins" method="post"> 
                    <input type="text" name="question_title" placeholder="question title"><br>
                    <input type="text" name="answer" placeholder="answer"><br> 
                    <input type="file" name="image" placeholder="add image"><br> 
                    <input type="text" name="true_answers" placeholder="write numbers of true answers split them by comma">  
                </form> 
            </div>
            ''' 
        )

own_answer_question_form = Template(
            '''
            <div>
                <form action="/$test_name/questoins" method="post"> 
                    <input type="text" name="question_title" placeholder="question title"><br> <input type="text" name="answer" placeholder="answer"><br> <input type="file" name="image" placeholder="add image"><br> </form> </div>
            ''' 
        )

add_new_question_link = Template('''<a href="/$test_name/$question_index">add new question</a>''')

new_test_form =  '''
                <form method="POST"> 
                    <input type="text" name="test_name" placeholder="test name">
                    <input type="submit" value="create test"> 
                </form> 
            '''

add_question_link = Template('''<a href="/$test_name/$questoin_index">  </a> ''')  
