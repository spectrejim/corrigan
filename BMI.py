import requests
from ast import literal_eval

def bmi(weight,height):
  return((weight/(height**2))*703)
def output(label,height,weight):
  short_wt=0
  avg_wt=0
  tall_wt=0
  short_bmi=0
  avg_bmi=0
  tall_bmi=0
  s=0
  a=0
  t=0
  for i in range(len(height)):
    if label[i]=="short":
      short_wt+=weight[i]
      short_bmi+=bmi(weight[i],height[i])
      s+=1
    elif label[i]=="avg":
      avg_wt+=weight[i]
      avg_bmi+=bmi(weight[i],height[i])
      a+=1
    else:
      tall_wt+=weight[i]
      tall_bmi+=bmi(weight[i],height[i])
      t+=1
      short_wt_kg=(short_wt/s)*0.453592
      avg_wt_kg=(avg_wt/a)*0.453592
      tall_wt_kg=(tall_wt/t)*0.453592
      short_bmi=short_bmi/s
      avg_bmi=avg_bmi/a
      tall_bmi=tall_bmi/t
      short_wt=short_wt/s
      avg_wt=avg_wt/a
      tall_wt=tall_wt/t
  print("Average weights:")
  print("Short People < 5’6”: {0} lbs ({1}kg). Average BMI: {2}".format(short_wt,short_wt_kg,short_bmi))
  print("Average People 5’6” and 6’0”: {0} lbs ({1}kg). Average BMI: {2}".format(avg_wt,avg_wt_kg,avg_bmi))
  print("Tall People >=6’0”: {0} lbs ({1} kg). Average BMI: {2}".format(tall_wt,tall_wt_kg,tall_bmi))

url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_25000.csv"
r=requests.get(url)
resp_list=r.text.split("\n")
resp_list=resp_list[1:]

p_dict={}
label=""
p_dict["weight"]=[]
p_dict["height"]=[]
p_dict["label"]=[]
for row in resp_list:
  if row=="":
    continue
  person=row.split(",")
  p_dict["height"].append(float(person[1]))
  p_dict["weight"].append(float(person[2]))
  if float(person[1]) < 66:
    p_dict["label"].append("short")
  elif float(person[1]) >= 66 and float(person[1]) < 72:
    p_dict["label"].append("avg")
  else:
    p_dict["label"].append("tall")

output(p_dict["label"],p_dict["height"],p_dict["weight"])


