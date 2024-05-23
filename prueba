import streamlit as st
from st_supabase_connection import SupabaseConnection

conn = st.connection("supabase",type=SupabaseConnection)
result = conn.client.table("users").select("*").execute()

st.write(result)
for row in result.data:
  st.write(f"{row['name']} has a password: {row['psw']}")
