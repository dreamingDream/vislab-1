import vislab
import pandas as pd
import os
_DIRNAME = vislab.config['paths']['shared_data']
DETAILED_DF_FILENAME = _DIRNAME + '/mine_flickr_df.h5'
groupNum = {'1604876@N25':8, '38514992@N00':10, '46353124@N00':6,  '907784@N22':5,'21563296@N00':11,  '42109523@N00':14,  '66108632@N00':13,  '978489@N20':12}
DIR = '/data/qzhang/imgs'

def get_images():
    images = {}
    imageIDs=[]
    cnt=0
    for groupn in os.listdir(DIR):
        groupDIR = os.path.join(DIR,groupn)
        num = groupNum[groupn]
        for imagen in os.listdir(groupDIR):
            imageID = imagen.split('.')[0]
            if imageID in imageIDs:
                cnt+=1                
            else: 
                imageIDs+=[imageID]
                images[groupn+'/'+imagen]=num
    print "\n\n dup count: \n\n",cnt
    return images
        
def _fetch_dataset(args=None):
    print('\nfetching Flickr dataset\n')
    images = get_images()
    df = pd.DataFrame([
        {
            'image_id': image.split('/')[1],
            'image_filename':os.path.join(DIR,image),
            'style': images[image]
        } for image in images
    ])
    df.index = pd.Index(df['image_id'], name='image_id')
    return df

def get_style_df(num=-1,force=False, args=None):
    print '\n\nhello\n\n'
    df = vislab.util.load_or_generate_df(
        DETAILED_DF_FILENAME, _fetch_dataset, force, args)
    #df = df.dropna(how='any', subset=['genre', 'style'])
    return df

