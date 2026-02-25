
# JOIN
# 1. Merge (seperti SQL JOIN) — berdasarkan kolom kunci
df_merged = pd.merge(df1, df2, on="ID")                    # inner join
df_merged = pd.merge(df1, df2, on="ID", how="left")        # left join
df_merged = pd.merge(df1, df2, on="ID", how="outer")       # full outer join
df_merged = pd.merge(df1, df2, left_on="id_a", right_on="id_b")  # kolom beda nama

# 2. Join — berdasarkan index
df_joined = df1.join(df2, how="left")
df_joined = df1.set_index("ID").join(df2.set_index("ID"))

# 3. Concat — tempel kolom (axis=1)
df_combined = pd.concat([df1, df2], axis=1)     # gabung samping (harus sama panjang/index)
df_combined = pd.concat([df1, df2], axis=0)     # gabung bawah (stack rows)