import requests
from bs4 import BeautifulSoup



def main_fun(URL):
    '''
    this function to repare the data and request it frome the page
    '''
    response = requests.get(URL)

    soup = BeautifulSoup(response.content, "html.parser")

    body = soup.find('body')
    

    citations = soup.find_all(class_='noprint Inline-Template Template-Fact')
    return citations


def get_citations_needed_count(URL):
    '''
    to count how many citation in the page 

    '''
    cite_reqs = main_fun(URL)
    return len(cite_reqs)


def get_citations_needed_report(URL):
        """
        to return the paragraph and the line that contain th citation
        """

        cite_report = main_fun(URL)
        citation_text = [citation.parent.text.strip() for citation in cite_report]
        
        para_ = '\n\n'.join([(citation_text[i]) for i in range(len(citation_text))])
        
        my_text =  [citation.previousSibling.strip() for citation in cite_report]

        line_ = '\n\n'.join([(my_text[i]) for i in range(len(my_text))])



        return f"the the paragraphs are :\n\n {para_} \n\n and the lines are \n\n{line_} "



if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
