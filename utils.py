import datetime 
import requests
import arxiv
import fitz

def get_citation_count(paper_name: str)->int:
    """
    Get the citation count of a paper from google scholar
    :param paper_name: the name of the paper
    :return: the citation count of the paper, None if the paper is not found or the request fails
    """
    url = f'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={paper_name}&btnG='
    response = requests.get(url)
    if response.status_code == 200:
        content = response.text
        citations = content.split('Cited by ')
        if len(citations) > 1:
            return int(citations[1].split('<')[0])
    else:
        return None    
    
def get_arxiv_results(paper_name: str, max_results: int = 3)->int:
    """
    Get results from arxiv search
    :param paper_name: the name of the paper
    :return: the results of the search, None if the search fails
    """
    client = arxiv.Client()
    search = arxiv.Search(query=paper_name, max_results=max_results, sort_by=arxiv.SortCriterion.Relevance)
    results = client.results(search)
    if results:
        return results
    return None

def get_paper_age(paper: arxiv.Result)->int:
    """
    Get the age of a paper
    :param paper: the paper
    :return: the age of the paper
    """
    return (datetime.datetime.now().year - paper.published.year)

def get_paper_text(paper: arxiv.Result)->str:
    """
    Get the text of a paper
    :param paper: the paper
    :return: the text of the paper
    """
    written_path = paper.download_pdf()
    with fitz.open(written_path) as pdf:
        text = ''
        for page in pdf:
            text += page.get_text()
    return text