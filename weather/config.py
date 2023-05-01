from pyspark.sql import SparkSession
from pyspark.sql import HiveContext


class config:

    def __init__(self):

        self.spark = SparkSession.builder.getOrCreate()
        self.sc = self.spark.sparkContext
        self.context = HiveContext(self.sc)
        self.key=",CA&APPID=2a2f1e754c02588897a5b262265e9353"

