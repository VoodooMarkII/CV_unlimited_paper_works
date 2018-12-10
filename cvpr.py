import bs4
import requests


def get_papers_info(url):
    """
    Generate the tuple which stores the information of papers in the given url.

    :param url: A String, url of the Open Access version of the conference.
           e.g. "http://openaccess.thecvf.com/CVPR2018.py" refers to  CVPR2018
    :return: A tuple of dict{'title': string,'pdf': string, 'supp': string}
    """
    rep = requests.get(url)
    rep.encoding = "utf-8"
    bs = bs4.BeautifulSoup(rep.text, "html.parser")
    titles = bs.find_all('dt', class_='ptitle')
    result = bs.find_all('dd')
    papers = []
    for title, link in zip(titles, result[1::2]):
        title = title.find('a').get_text()
        if link.find('a', text='pdf'):
            pdf_link = link.find('a', text='pdf').get('href')
        else:
            pdf_link = None
        if link.find('a', text='supp'):
            supp_link = link.find('a', text='supp').get('href')
        else:
            supp_link = None
        papers.append({'title': title, 'pdf': pdf_link, 'supp': supp_link})
    return papers


def download_paper(papers):
    """
    Download the papers in the papers parameter.

    The value of 'pdf' and 'supp' key is the last half of the file's url,
    e.g. content_cvpr_2018/papers/Das_Embodied_Question_Answering_CVPR_2018_paper.pdf, NOT the complete url.

    :param papers: A tuple of dict{'title': string,'pdf': string, 'supp': string}
    :return: None
    """

    dl_link_prefix = "http://openaccess.thecvf.com/"
    total_paper_num = len(papers)
    for idx, paper in enumerate(papers):
        pdf_filename = paper['title'].replace(' ', '_') + '.pdf'
        supp_filename = paper['title'].replace(' ', '_') + '_supp.pdf'

        print("Downloading %s, %d of %d papers." % (pdf_filename, idx + 1, total_paper_num))
        paper_r = requests.get(dl_link_prefix + paper['pdf'])
        with open(pdf_filename, 'wb') as f:
            f.write(paper_r.content)
        if paper['supp'] is not None:
            print("Downloading %s supplemental material, %d of %d papers." % (pdf_filename, idx + 1, total_paper_num))
            supp_r = requests.get(dl_link_prefix + paper['supp'])
            with open(supp_filename, 'wb')as f:
                f.write(supp_r.content)


if __name__ == '__main__':
    papers_info = get_papers_info("http://openaccess.thecvf.com/CVPR2018.py")
    download_paper(papers_info)
