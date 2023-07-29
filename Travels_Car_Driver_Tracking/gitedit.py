import streamlit as st

st.title('Try to add text')

def write(text):
    f = open('edit_file.txt','a')
    f.write('New input: {}\n'.format(text))
    f.close()

def get_file():
    f = open('edit_file.txt','r')
    r = f.read()
    f.close()
    return r

text = st.text_input('Text')
st.button('Add text to file',on_click = write,args = [text])

st.download_button('Download text',get_file(),'text_file.txt')




# from github import Github
# from github import Auth
# import streamlit as st

# st.write(st.experimental_user)

# GITHUB_REPO = 'Travels_Car_Driver_Tracking'
# GITHUB_TOKEN = st.secrets["GITHUB_TOKEN"]

# auth = Auth.Token(GITHUB_TOKEN)
# g = Github(auth=auth)


# st.title('Try to add text to GitHub')

# def write(text):
#     r, rf,ft = get_file()
#     t = ft + text
#     r.update_file(rf.path,'streamlit commit',t,rf.sha,branch='main')
    

# def get_file():
#     repo = g.get_user().get_repo(GITHUB_REPO)
#     repo_file = repo.get_contents('tests/test_1.txt')
#     file_text = repo_file.decoded_content.decode()
#     return repo, repo_file, file_text

# text = st.text_input('Text')
# st.button('Add text to file',on_click = write,args = [text])

# # st.download_button('Download repo_file',get_file()[1],'repo_file.txt')
# st.download_button('Download file_text',get_file()[2],'file_text.txt')


# # using an access token

# # First create a Github instance:

# # Public Web Github

# # all_files = []
# # contents = repo.get_contents("tests/test_1.txt")

# # print(contents)
# # new_text = contents.decoded_content.decode() + '\nAdding stuff'

# # repo.update_file(contents.path,'Adding stuff',new_text,contents.sha,branch='main')
