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

    # else:
    #     raise ValueError("enter a valid unit of weight")



    if unit_of_height =='m': 
     height_in_m = height

    elif unit_of_height == 'cm': 
     height_in_m = height/100

    elif unit_of_height == 'inches':
     height_in_m = round((height*0.0254),3)

    
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



@app.route('/', methods=['POST', 'GET'])
def bmi_cal():
    weight = request.form.get('weight')
    unit_of_weight = request.form.get('unit of weight')
    height = request.form.get('height')
    unit_of_height = request.form.get('unit of height')
    if float(weight) > 0 and float(height) > 0:
        try:

            weight = float(weight) 
            height = float(height) 
           
        except ValueError:
            error_message = "Please enter valid weight and height values."
            return render_template('index.html', error_message=error_message)

        if unit_of_weight not in ['kg', 'g', 'lb'] or unit_of_height not in ['m', 'cm', 'inches']:
            error_message = "Please enter valid units for weight and height."
            return render_template('index.html', error_message=error_message)

        bmi_condition = bmi_data(weight, unit_of_weight, height, unit_of_height)
        

        bmi_test = bmi_result(bmi_condition)
        return render_template('index.html',
        weight_and_unit=f'{weight}{unit_of_weight}',
        height_and_unit=f'{height}{unit_of_height}',
        bmi_status=bmi_test)

    else:
        error_message = "Please enter valid height and weight, value must greater than 0."
        return render_template('index.html', error_message=error_message)



if __name__ == '__main__':
    app.run(debug=True, port=9000)



if __name__ == '__main__':
    app.run(debug=True)
    