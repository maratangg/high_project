# !pip install koreanize_matplotlib
def settins():
    import warnings
    import koreanize_matplotlib
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as  plt
    from matplotlib_venn import venn2
    import plotly.express as px
    import plotly.graph_objects as go
    import ast
    
    
    # # 그래프 해상도 높이기
    # try:
    #     # %config InlineBackend.figure_format = 'retina'
    # except Exception as e:
    #     print(f'💩 {e}')



    # 경고 무시
    warnings.filterwarnings("ignore")
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)  # 출력할 너비를 넉넉하게 조정
    pd.set_option('display.expand_frame_repr', False)  # 옆으로 길어져도 줄바꿈 없이 출력
    pd.set_option('display.max_colwidth', None)  # 긴 문자열도 생략 없이 출력

    try:
        from google.colab import drive
        drive.mount('/content/drive')

        import os
        os.chdir('/content/drive/MyDrive/파트4')
        print('✅ Succesful access google_drive_directory')
        
    except Exception as e:
        print('🤗 Hello vscode')
        
## get_df 함수
def get_df(db_name, table_name, API_KEY_PATH):
    import pandas as pd  # pandas 임포트

    if table_name in ['accounts_user', 'accounts_blockrecord']:
        table_name = pd.read_parquet(
            f"gs://high_project/{db_name}/{table_name}.parquet", 
            storage_options={'token' : API_KEY_PATH})
    else:
        table_name = pd.read_csv(
            f"gs://high_project/{db_name}/{table_name}.csv",
            storage_options={'token' : API_KEY_PATH}
            )
    return table_name

## literal_eval 형변환 함수
def to_literal_eval(df, column):
    return  df[column].apply(lambda x: ast.literal_eval(x) if x != '[]' else [])


# 리스트 내에 드랍 유저가 있는지 확인하는 함수
def find_drop_users(df, column):
    drop_users = [831956, 1580627, 1580689, 1580626, 995177]
    print(f'{column}:')
    for i in drop_users:
        count_drop_rows = len(df[df[column].apply(lambda x: i in x)])
        if count_drop_rows != 0:
            print(f"‼️ 관리자 {i}가 포함된 행 {count_drop_rows}개 존재")
        else:
            print(f"✅ 관리자 {i} 포함행 없음")