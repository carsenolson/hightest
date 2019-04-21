from string import Template


nav = Template(
        '''
            <!DOCTYPE html>
            <html>
                <head> 
                    <meta charset="utf-8">   
                    <link rel="stylesheet" type="text/css" href="$static_path/style.css"> 
                </head> 
                <body> 
                    <h3>$page_name </h3>  
        '''
        )
test_list = Template('''<a href="/$test_name/">$test_name</a><br>''')

question_list = Template(
            ''' 
            <div class="question">
                <a href="/$test_name/questions">$question_title</a>
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

footer = Template(
            '''
                    <script src="$static_path/main.js"> 
                </body> 
            ''' 
        )

new_test_form =  '''
                <form method="post"> 
                    <input type="text" name="test_name" placeholder="test name">
                    <input type="submit" value="create test"> 
                </form> 
            '''

add_question_link = Template('''<a href="/$test_name/$questoin_index">  </a> ''')  
