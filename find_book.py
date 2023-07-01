import requests

def recherche_livre(query):
    url = 'http://openlibrary.org/search.json'
    params = {
        'q': query
    }

    reponse = requests.get(url, params=params)
    data = reponse.json()
    for doc in data['docs']:
        title = doc['title']
        author = doc['author_name'][0] if 'author_name' in doc else 'N/A'
        print(f'Titre: {title}')
        print(f'Auteur: {author}')
        print('---')


recherche = input("Le livre que vous chercher :")

recherche_livre(recherche)




#                                               
#                                                ██████████████                          
#                                        ████████▓▓▓▓██░░░░██▓▓████                      
#                                ████████░░░░░░░░██▓▓██░░░░██▓▓▓▓▓▓██                    
#                            ████░░██▓▓▓▓██░░░░░░██▓▓▓▓██░░██▓▓▓▓▓▓▓▓██                  
#                        ████░░░░░░░░██▓▓▓▓██░░░░██▓▓▓▓██░░██▓▓▓▓▓▓▓▓██                  
#                      ██▓▓▓▓██░░░░░░░░██▓▓▓▓██░░██▓▓▓▓██░░██▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓██░░░░░░██▓▓▓▓██░░██▓▓▓▓██░░██▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓▓▓██░░░░██▓▓▓▓██░░██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓██░░██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                      
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                        
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                            
#                      ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                                
#                          ████████▓▓▓▓▓▓▓▓▓▓▓▓██████                                    
#                                  ████████████           