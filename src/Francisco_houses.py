import pandas as pd


train_data = pd.read_csv('data/raw/train.csv')
test__data = pd.read_csv('data/raw/test.csv')


from pyspark.sql import SparkSession
from pyspark import SparkConf, SparkContext
spark = SparkSession \
.builder \
.master("local")\
.appName("FranciscoApp") \
.getOrCreate()
sc = SparkContext.getOrCreate(SparkConf().setAppName("my app").setMaster("local[*]"))
