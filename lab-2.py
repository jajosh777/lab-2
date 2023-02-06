def main():
    My_info={
        'name' : 'JayJoshi',
        'F_name':'jay',
        'country': 'India',
        'student_id':'10275351'
            },
    {
        'pizza toppings':
        [
            'cheese',
            'paneer',
            'extra cheeeesee...haaaha'
        ],
       'movies':
        [
           {
            'movie':'intersteller',
            'genre':'sci-fic' 
           },
           {
            'movie2':'avengers',
            'genre_2':'superhero film'
           },
           {
            'movie3':'fast and furious',
            'genre_3' : 'action'
           }
        ],
    }
    print_student_name_and_id(My_info)
    print_pizza_toppings(My_info)
    add_pizza_toppings(My_info)
    print_movie_titles(My_info)
    return
def print_student_name_and_id(My_info):
    full_name= My_info['name']
    first_name= My_info['F_name'] 
    Student_id= My_info['student_id']
    print(f'My name is {full_name}, but you can call me Mr. {first_name}')
    print(f'My student ID is {Student_id}')
    return    

def add_pizza_toppings(My_info, toppings):
     My_info['pizza toppings':'cheese'].extend(toppings)
     My_info['pizza toppings':'paneer']
     My_info['pizza toppings':'extra cheeeesee...haaaha']
     toppings (tuple()).sort
     toppings(str.casefold())
     print(f'My favorite pizza topings are:{toppings}')
     return 

def print_pizza_toppings(My_info):
   print(f'My favorite pizza topings are:{My_info}')
   return 

def print_movie_titles(My_info):
        movie_1_genre=My_info['movies':'intersteller']
        movie_2_genre=My_info['movies':'avengers']
        movie_3_genre=My_info['movies':'fast and furious']
        print(f'i like to watch{movie_1_genre},{movie_2_genre},{movie_3_genre}')

        return 

   
    
if __name__ == '__main__':
 main()