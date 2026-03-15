from pyspark import pipelines as dp

@dp.table
def transformed():
  return spark.range(10)