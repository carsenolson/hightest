from string import Template

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
                    <input type="text" name="question_title" placeholder="question title"><br>
                    <input type="text" name="answer" placeholder="answer"><br> 
                    <input type="file" name="image" placeholder="add image"><br> 
                </form> 
            </div>
            ''' 
        )
