from langchain.embeddings.openai import OpenAIEmbeddings

embedding_txt = "测试" * 20000

embeddings = OpenAIEmbeddings(model='text-embedding-ada-002')
# embeddings = OpenAIEmbeddings(deployment="embeddingv2", model='text-embedding-ada-002', chunk_size=1)

try:
    txt_arr_embedding = embeddings.embed_documents([embedding_txt])
    print(txt_arr_embedding[0])
except Exception as e:
    print(type(e))

if __name__ == '__main__':
    pass
