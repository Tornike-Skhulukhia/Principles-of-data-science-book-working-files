from requests_html import HTMLSession
import pandas as pd
import matplotlib.pyplot as plt


def get_titles_for_all_categories(lang='ge', drop_all_duplicates=True):
    '''
    For Georgian job posts only,
    '''
    data = []
    # ids_by_cats = {}

    s = HTMLSession()
    base_url = f"https://jobs.ge/{lang}/"  # en or ge
    resp_1 = s.get(base_url) 

    cats_info = {i.attrs['value']:
                 i.text for i in resp_1.html.find('select[name="cid"] option:not([value=""])')}
    # print(cats_info)
    url = base_url + '?page={}&q=&cid={}&lid=&jid='
    elem_selector = f"a[href^='/{lang}/?view=jobs&id']:not([target='_blank'])"

    for cat_id, cat_name in cats_info.items():
        print(cat_name, "started")
        cat_titles_list = []
        job_ids = []
        page_num = 1

        elems = s.get(url.format(page_num, cat_id)).html.find(elem_selector)
        page_ids = {int(i.attrs['href'].split('id=')[-1]) for i in elems}

        # until we find new ids
        while page_ids - set(job_ids):
            print(page_num, "+")
            job_ids.extend(page_ids)
            cat_titles_list.extend([i.text for i in elems])

            page_num += 1
            elems = s.get(url.format(page_num, cat_id)).html.find(elem_selector)
            page_ids = {int(i.attrs['href'].split('id=')[-1]) for i in elems}

        # ids_by_cats[cat_name] = job_ids
        data.extend([{'category': cat_name, 'title': title, 'id': id_}
                     for title, id_ in zip(cat_titles_list, job_ids)])

    # do not include titles with posts in more than one category 
    df = pd.DataFrame(data)
    if drop_all_duplicates: df = df.drop_duplicates(subset='id', keep=False)

    return df


# df = get_titles_for_all_categories(lang='en')

# from info_ import df


# # venn diagrams
# from info_ import ids_by_cats, titles_by_cats

# for cat_name, cat_ids in ids_by_cats.items():
#     for other_cat_name, other_cat_ids in ids_by_cats.items():
#         if other_cat_name == cat_name: continue

#         common_items_num = len(set(cat_ids).intersection(set(other_cat_ids)))

#         if common_items_num:
#             print(cat_name, other_cat_name, common_items_num, sep=" | ")
