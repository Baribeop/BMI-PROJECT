from flask import Flask, request, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")



def data_bmi(weight, unit_of_weight, height, unit_of_height):

    if unit_of_weight == "kg":
     weight_in_kg = weight

    elif unit_of_weight=="g": 
     weight_in_kg  = (weight/1000)

    elif unit_of_weight == "lb": 
     weight_in_kg  = round((weight*0.453),3)
   
    
    if unit_of_height =='m': 
     height_in_m = height

    elif unit_of_height == 'cm': 
     height_in_m = height/100

    elif unit_of_height == 'inches':
     height_in_m = round((height*0.0254),3)
    
    # else:

    #  error_message = "enter valid height"
    
    bmi_val = round((weight_in_kg)/(height_in_m)**2 ,2)
    
    return bmi_val
    

def val_bmi(bmi_val):
    
    if bmi_val < 18.5:
     bmi_status = [f'Your body mass index is {bmi_val} kilogram per metre square,you are considered underweight and possibly malnourished']
    elif 18.5 <= bmi_val <= 24.9:
     bmi_status = [f'Your body mass index is {bmi_val} kilogram per metre square, you are within a healthy weight']
    elif 25.0 <= bmi_val <= 29.9:
     bmi_status = [f'Your body mass index is {bmi_val} kilogram per metre square, you are considered overweight']
    if bmi_val >=30: 
     bmi_status = [f'Your body mass index is {bmi_val} kilogram per metre square, you are considered obese']
    
    return bmi_status


@app.route('/', methods = ['POST'])    
def bmi_cal():
    weight = float(request.form['weight'])
    unit_of_weight = str(request.form['unit of weight'].lower())
    height = float(request.form['height'])
    unit_of_height = str(request.form['unit of height'].lower())
    bmi_cond = data_bmi(weight, unit_of_weight, height, unit_of_height)
    bmi_cal = val_bmi(bmi_cond)
    return render_template('index.html', weight_and_unit = f'{weight}{unit_of_weight}',
                           height_and_unit=f'{height}{unit_of_height}', bmi_status = bmi_cal)


if __name__ == '__main__':
    app.run(debug=True)
    