import React, {useState} from 'react';
import {ScrollView, StyleSheet, View} from 'react-native';
import DatePicker from 'react-native-date-picker';
import {Button, TextInput, Title} from 'react-native-paper';
import {useSelector} from 'react-redux';
import FormikOptions from '../../components/buildings_map/FormikOptions';
import FormikTextField from '../../components/buildings_map/FormikTextField';
import {COLORS} from '../../core/theme';
import useBuildingSurvey from '../../hooks/useBuildingSurvey';
import {Header} from '../../components/headers';
import {t} from '../../i18n';

const BuildingSurveyScreen = () => {
  const {contentsLabel} = useSelector(state => state.auth);
  const getLabel = key => t(key, contentsLabel);
  const {
    formik: {values, setFieldValue, errors},
  } = useBuildingSurvey();

  const [dateModal, setDateModal] = useState(false);
  const [constructionModal, setConstructionModal] = useState(false);

  return (
    <View style={{flex: 1}}>
      <Header title={getLabel('Building Survey Form')} />
      <ScrollView style={styles.container}>
        <FormikOptions
          title={getLabel('Is main building?')}
          value={values.is_main_building}
          error={errors.is_main_building}
          options={[
            {value: false, label: getLabel('No')},
            {value: true, label: getLabel('Yes')},
          ]}
          setFieldValue={val => setFieldValue('is_main_building', val)}
        />
        {!values.is_main_building && <FormikTextField title={getLabel('Building no')} />}
        <FormikTextField title={getLabel('Tax code')} />
        <FormikOptions title={getLabel('Select ward no')} />
        <FormikTextField title={getLabel('Street name')} />
        <FormikOptions title={getLabel('Select structure type')} />
        <FormikTextField title={getLabel('Number of floors')} keyboardType="number-pad" />
        <FormikOptions
          title={getLabel('Functional use of building')}
          value={values.functional_use}
          error={errors.is_main_building}
          options={[
            {value: '', label: getLabel('Select functional use')},
            {value: 'health', label: getLabel('Health')},
            {value: 'business', label: getLabel('Business')},
            {value: 'residental', label: getLabel('Residental')},
          ]}
          setFieldValue={val => setFieldValue('functional_use', val)}
        />
        <FormikOptions
          title={getLabel('Use of building category')}
          options={[
            {value: 'Option 1', label: 'Option 1'},
            {value: 'Option 2', label: 'Option 2'},
            {value: 'Option 3', label: 'Option 3'},
            {value: 'Option 4', label: 'Option 4'},
          ]}
          value={values.building_use}
          setFieldValue={val => setFieldValue('building_use', val)}
        />
        {values.functional_use && values.functional_use !== 'residental' ? (
          <FormikTextField title={getLabel('Office or business name')} />
        ) : null}
        <FormikTextField title={getLabel('Number of households')} />
        <FormikTextField title={getLabel('Total population of building')} />
        <FormikTextField
          title={getLabel('Survyed date')}
          editable={false}
          right={
            <TextInput.Icon
              icon="calendar"
              onPress={() => setDateModal(true)}
            />
          }
        />
        <DatePicker
          date={new Date()}
          onCancel={() => setDateModal(false)}
          maximumDate={new Date()}
          modal
          open={dateModal}
        />
        <FormikOptions
          title={getLabel('Sanitation System Technology')}
          value={values.technology}
          options={[
            {value: '0', label: getLabel('Select sanitation system technology')},
            {value: '1', label: getLabel('Anaerobic Digestor')},
            {value: '2', label: getLabel('Cesspool/Holding tank')},
            {value: '3', label: getLabel('Communal Septic Tank (from PT CT)')},
            {value: '4', label: getLabel('Dehydration Toilet System')},
            {value: '5', label: 'DEWATS Online'},
            {value: '6', label: getLabel('Directly to natural water body')},
            {value: '7', label: getLabel('Directly to sewage network')},
            {value: '8', label: getLabel('Directly to stormwater draim')},
            {value: '9', label: getLabel('Directly to surrounding environment')},
            {value: '10', label: getLabel('Double pit with soak away pit')},
            {value: '11', label: getLabel('Septic tank connected to sewerage network')},
            {value: '12', label: getLabel('Septic tank without soak away pit')},
            {value: '13', label: getLabel('Septic tank with soak away pit')},
            {value: '14', label: getLabel('Shared Septic tank')},
            {value: '115', label: getLabel('Single pit')},
            ,
          ]}
          setFieldValue={val => setFieldValue('technology', val)}
          error={errors.technology}
        />
        {values.technology === '13' && (
          <FormikTextField title={getLabel('BIN of pre-connected buildings')} />
        )}
        {values.technology === '8' && <FormikTextField title={getLabel('Drain code')} />}
        {values.technology === '11' && <FormikTextField title={getLabel('Sewer code')} />}
        {values.technology === '2' ||
          values.technology === '11' ||
          (values.technology === '12' && (
            <View style={styles.containment}>
              <Title style={styles.title}>{getLabel('Containment information')}</Title>
              <FormikTextField title={getLabel('Length')} />
              <FormikTextField title={getLabel('Width')} />
              <FormikTextField title={getLabel('Depth')} />
              <FormikTextField title={getLabel('Volume(m3)')} />
              <FormikOptions title={getLabel('Containment location')} />
              <FormikOptions title={getLabel('Septic tank compliance')} />
              <FormikTextField
                title={getLabel('Construction date')}
                editable={false}
                right={
                  <TextInput.Icon
                    icon="calendar"
                    onPress={() => setDateModal(true)}
                  />
                }
              />
              <DatePicker
                date={new Date()}
                onCancel={() => setConstructionModal(false)}
                maximumDate={new Date()}
                modal
                open={constructionModal}
              />
            </View>
          ))}
        {values.technology === '10' ||
          (values.technology === '15' && (
            <View style={styles.containment}>
              <Title style={styles.title}>{getLabel('Containment information')}</Title>
              <FormikTextField title={getLabel('Pit diameter')} />
              <FormikTextField title={getLabel('Pit depth')} />
              <FormikTextField title={getLabel('Volume(m3)')} />
              <FormikOptions
                title={getLabel('Containment location')}
                value={values.containment_location}
                error={errors.containment_location}
                setFieldValue={val =>
                  setFieldValue('containment_location', val)
                }
                options={[
                  {
                    value: '',
                    label: getLabel('Select containment location'),
                  },
                  {
                    value: 'outside',
                    label: getLabel('Outside building footprint'),
                  },
                  {
                    value: 'inside',
                    label: getLabel('Inside building footprint'),
                  },
                  {
                    value: 'outside_2',
                    label: getLabel('Outside property boundary'),
                  },
                ]}
              />
              <FormikOptions
                title={getLabel('Septic tank compliance')}
                value={values.compliance}
                error={errors.compliance}
                setFieldValue={val => setFieldValue('compliance', val)}
                options={[
                  {
                    value: false,
                    label: getLabel('No'),
                  },
                  {
                    value: true,
                    label: getLabel('Yes'),
                  },
                ]}
              />
              <FormikTextField
                title={getLabel('Construction date')}
                editable={false}
                right={
                  <TextInput.Icon
                    icon="calendar"
                    onPress={() => setDateModal(true)}
                  />
                }
              />
              <DatePicker
                date={new Date()}
                onCancel={() => setConstructionModal(false)}
                maximumDate={new Date()}
                modal
                open={constructionModal}
              />
            </View>
          ))}
        {values.technology === '2' ||
          values.technology === '10' ||
          values.technology === '11' ||
          values.technology === '12' ||
          values.technology === '13' ||
          values.technology === '14' ||
          (values.technology === '15' && (
            <FormikOptions
              title={getLabel('Is Building Vacutug accessible')}
              value={values.vacutug_accessible}
              setFieldValue={val => setFieldValue('vacutug_accessible', val)}
              options={[
                {
                  value: 'no',
                  label: getLabel('No'),
                  value: 'yes',
                  label: getLabel('Yes'),
                  value: 'dontknow',
                  label: getLabel("Don't know"),
                },
              ]}
            />
          ))}
        <FormikOptions title={getLabel('Public/Community Toilet Name')} />
        {values.technology !== '3' &&
          values.technology !== '6' &&
          values.technology !== '0' &&
          values.technology !== '8' &&
          values.technology !== '9' && (
            <FormikTextField title={getLabel('Total number of toilets')} />
          )}
        <FormikOptions title={getLabel('Main Drinking Water source')} />
        <FormikOptions title={getLabel('Well Presence')} />
        <FormikTextField title={getLabel('Distance of containment from well (m)')} />
        <FormikTextField title={getLabel('Water supply Customer ID')} />
        <FormikTextField title={getLabel('SWM supply Customer ID')} />
        <FormikTextField title={getLabel('Owner name')} />
        <FormikOptions title={getLabel('Gender')} />
        <FormikTextField title={getLabel('Contact number')} />
        <Button mode="contained" style={styles.button}>
          {getLabel('Save')}
        </Button>
      </ScrollView>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 10,
  },
  picker: {
    elevation: 3,
    marginVertical: 1,
    marginHorizontal: 2,
    borderRadius: 10,
    backgroundColor: COLORS.light,
  },
  inputText: {
    fontSize: 15,
    marginVertical: 5,
    fontWeight: 'bold',
  },
  input: {
    backgroundColor: COLORS.light,
    marginVertical: 1,
  },
  errorText: {
    color: COLORS.error,
    fontSize: 13,
  },
  containment: {
    marginTop: 10,
    marginBottom: 25,
  },
  title: {
    marginVertical: 5,
  },
  button: {
    marginTop: 10,
    marginBottom: 30,
    width: '60%',
  },
});

export default BuildingSurveyScreen;
