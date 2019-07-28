import xlrd
from openpyxl import load_workbook
from tweepy_fetch import TweepyFetcher

# EXCEL FILE LOCATION
loc = r"C:\Users\Dheepthaa\Desktop\twitter_dataset2_urls.xlsx"

# EXCEL WORKBOOK
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

for i in range(0, sheet.nrows):

    # EXCEL DATA READING
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    id = (sheet.cell_value(i, 0).split(".com/", 1)[1])
    print("\n\nRESPONSE FOR ID : " + id)

    try:
        # FETCH ATTRIBUTES FOR ID
        (followers, friends, avg_retweets, avg_likes, bio, profile_pic, first_search_result, retweet_fraction,
         avg_no_urls, isVerified) = TweepyFetcher().fetch(id)

        # EXCEL DATA WRITING
        wb = load_workbook(filename=loc)
        sheet = wb['Sheet1']
        row = (i+1)
        sheet['B'+str(row)] = followers
        sheet['C'+str(row)] = friends
        if followers+friends != 0:
            sheet['D'+str(row)] = followers / (followers+friends)
            sheet['E' + str(row)] = friends / (followers + friends)
        else:
            sheet['D' + str(row)] = 0
            sheet['E' + str(row)] = 0
        sheet['F'+str(row)] = avg_retweets
        sheet['G'+str(row)] = avg_likes
        sheet['H' + str(row)] = bio
        sheet['I' + str(row)] = profile_pic
        sheet['J' + str(row)] = first_search_result
        sheet['K' + str(row)] = retweet_fraction
        sheet['L' + str(row)] = avg_no_urls

        # EXCEL SAVE
        wb.save(loc)

    except:
        pass





