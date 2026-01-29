from behave import given, when, then
from app import app

@given('aplikacja webowa jest uruchomiona')
def step_impl(context):
    app.testing = True
    context.client = app.test_client()
    context.form_data = {'waluta': '', 'okres': 'tydzien'}

@when('użytkownik wprowadzi walutę "{waluta}"')
def step_impl(context, waluta):
    context.form_data['waluta'] = waluta

@when('użytkownik pozostawi pole waluty puste')
def step_impl(context):
    context.form_data['waluta'] = ''

@when('wybierze okres "{okres}"')
def step_impl(context, okres):
    context.form_data['okres'] = okres

@when('wyśle formularz')
def step_impl(context):
    context.response = context.client.post('/pobierz', data=context.form_data, follow_redirects=True)

@then('system powinien wyświetlić listę kursów historycznych')
def step_impl(context):
    assert context.response.status_code == 200
    assert b'wyniki' in context.response.data
    print("Sukces: Wyniki są widoczne.")

@then('system powinien wyświetlić błąd "{wiadomosc}"')
def step_impl(context, wiadomosc):
    response_text = context.response.data.decode('utf-8')
    assert wiadomosc in response_text
    print(f"Sukces: Wyświetlono oczekiwany błąd: {wiadomosc}")

@then('system nie powinien wysłać zapytania i poprosić o wypełnienie pola')
def step_impl(context):
    assert b'wyniki' not in context.response.data
    assert b'required' in context.response.data
    print("Sukces: Formularz zablokował puste zapytanie.")