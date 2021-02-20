
from flask import render_template, request, redirect, url_for, session, current_app as app
from app.forms import InputForm, DataForm
from app.states_region import state_region
from app.model import predict_rent
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('./app/artifacts/craigstimate-301619-firebase-adminsdk-wz27w-47e423419f.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://craigstimate-301619-default-rtdb.firebaseio.com/'
})


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    
    form.state.choices = [(k.upper()) for k, v in state_region.items()]


    if request.method == 'POST':
        return redirect(url_for('get_data', state=request.form.get('state')))

    
    context = {
        'form' : form,
    }

    return render_template('index.html', **context)


@app.route('/form', methods=['GET', 'POST'])
def get_data():
    form = DataForm()
    context = {
        'form': form,
    }
    if request.method == 'GET':
        state = request.args.get('state').lower()
        
        if state in state_region:
            display = [i.title() for i in state_region[state]]
            values = [i for i in state_region[state]]
            form.region.choices = list(zip(values, display))
        # print(state)
        
        return render_template('form.html', **context, state=state)
        
    
    if request.method == 'POST':
        
        context = {
            'region' : form.region.data,
            'home_type' : form.home_type.data,
            'squarefeet' : int(form.sqfeet.data),
            'beds' : form.bed.data,
            'baths' : form.bath.data,
            'pets' : form.pet.data,
            'smoke' : form.smoke.data,
            'laundry' : form.laundry.data,
            'parking' : form.parking.data,

        }

        return redirect(url_for('predict', **context))



@app.route('/predict', methods=['GET', 'POST'])
def predict():
    
    '''
    For Predicting and rendering results on HTML 
    '''

    form = InputForm()
    form.state.choices = [(k.upper()) for k, v in state_region.items()]
    
    ## Get back the state_name; look up by value, not ideal, need a better way to do this
    def get_key(value):
        for k,v in state_region.items():
            for i in v:
                if  value == i:
                    state_name = k
                    return state_name.upper()

    #use form data to make the prediction
    state_name = get_key(request.args['region'])
    region = request.args['region']
    home_type = request.args['home_type'].lower()
    squarefeet = request.args['squarefeet']
    beds = request.args['beds']
    baths = request.args['baths']
    pets = request.args['pets']
    smoke = request.args['smoke']
    laundry = request.args['laundry'].lower()
    parking = request.args['parking'].lower()
    
    features = [region, home_type, squarefeet,
                beds, baths, pets, smoke, laundry, parking]

    prediction = predict_rent(region, home_type, squarefeet, beds, baths, pets, smoke, laundry, parking)

    ### Submitting User Input to Firebase, initialize db and collection ###
    ref = db.reference('/user_input')

    #Submits data to Firebabse
    ref.push({

        'state': state_name,
        'region': region,
        'home_type': home_type,
        'squarefeet': squarefeet,
        'beds': beds,
        'baths': baths,
        'pets': pets,
        'smoke': smoke,
        'laundry': laundry,
        'parking': parking,

    })

    
    return render_template('index.html', prediction_text=f'{prediction}', features=features, form=form, state_name=state_name)
