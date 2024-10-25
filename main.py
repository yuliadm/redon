import search_query_creator
import utils

def big_pipeline(query: str)-> list[dict]:
    search_query = search_query_creator.create_search_query_from_question(query)
    search_results = utils.get_arxiv_results(search_query)
    result_dict = []
    for result in search_results:
        print(result.title)
        university_name = search_query_creator.extract_university(utils.get_paper_text(result)[:200])
        result_dict.append({
            "title": result.title,
            "citation_count": utils.get_citation_count(result.title),
            "age": utils.get_paper_age(result),
            "university": university_name,
            "ranking": utils.get_uni_ranking(university_name) if university_name is not None else 0,
            "url": result.pdf_url if result.pdf_url else "DOI:" + result.doi
        })
    return result_dict