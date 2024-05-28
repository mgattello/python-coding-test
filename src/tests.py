# Write your tests here
import unittest
from fastapi.testclient import TestClient
from main import app
from ipdf_service import IPdfService
from idiff_lib import IDiffLib
from src.utils import *

client = TestClient(app)

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.expectedObj = {
            'Company_Name': 'RetailCo',
            'Industry': 'Retail',
            'Market_Capitalization': '2000',
            'Revenue_in_millions': '800',
            'EBITDA_in_millions': '150',
            'Net_Income_in_millions': '40',
            'Debt_in_millions': '110',
            'Equity_in_millions': '400',
            'Enterprise_Value_in_millions': '2100',
            'P_E_Ratio': '20',
            'Revenue_Growth_Rate_%': '8',
            'EBITDA_Margin_%': '18.75',
            'ROE_Return_on_Equity_%': '10',
            'ROA_Return_on_Assets_%': '6.5',
            'Current_Ratio': '1.8',
            'Debt_to_Equity_Ratio': '0.25',
            'Location': 'Chicago, IL',
            'CEO': 'Bob Johnson',
            'Number_of_Employees': '2000'
        }

    def test_get_200_retailco(self):
        response = client.get('/difference/retailco')
        expected = {
            "dataFromPDF": {
                "Company_Name": "RetailCo",
                "Industry": null,
                "Market_Capitalization": "2000",
                "Revenue_in_millions": "800",
                "EBITDA_in_millions": "150",
                "Net_Income_in_millions": "40",
                "Debt_in_millions": "110",
                "Equity_in_millions": "400",
                "Enterprise_Value_in_millions": "2100",
                "P_E_Ratio": "20",
                "Revenue_Growth_Rate": null,
                "EBITDA_Margin": null,
                "ROE_Return_on_Equity": null,
                "ROA_Return_on_Assets": null,
                "Current_Ratio": "1.8",
                "Debt_to_Equity_Ratio": "0.25",
                "Location": null,
                "CEO": null,
                "Number_of_Employees": "2000"
            },
            "dataFromDatabase": {
                "Company_Name": "RetailCo",
                "Industry": null,
                "Market_Capitalization": "2000",
                "Revenue_in_millions": "800",
                "EBITDA_in_millions": "150",
                "Net_Income_in_millions": "40",
                "Debt_in_millions": "100",
                "Equity_in_millions": "400",
                "Enterprise_Value_in_millions": "2100",
                "P_E_Ratio": "20",
                "Revenue_Growth_Rate": null,
                "EBITDA_Margin": null,
                "Net_Income_Margin": null,
                "ROE_Return_on_Equity": null,
                "ROA_Return_on_Assets": null,
                "Current_Ratio": "1.8",
                "Debt_to_Equity_Ratio": "0.25",
                "Location": null
            },
            "delta": [
                "Debt_in_millions",
                "Net_Income_Margin_%",
                "Number_of_Employees"
            ]
        }
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {})

    def test_get_200_financellc(self):
        response = client.get('/difference/financellc')   
        self.assertEqual(response.status_code, 200)
    
    def test_get_200_healthinc(self):
        response = client.get('/difference/healthinc')   
        self.assertEqual(response.status_code, 200)
    
    def test_get_500_techcorp(self):
        response = client.get('/difference/techcorp')   
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.text, '{"detail":"Error: File AssetParamEnum.techcorp not found"}')

    def test_get_404_when_paran_asset_is_empty(self):
        response = client.get('/difference')
        self.assertEqual(response.status_code, 404)
    
    def test_get_422_when_paran_asset_not_included_enum(self):
        response = client.get('/difference/test')
        self.assertEqual(response.status_code, 422)

    def test_when_get_data_then_is_object(self):
        data = IPdfService(file_path = 'retailco')
        self.assertEqual(data.get_data(), {
            'Company_Name': 'RetailCo',
            'Current_Ratio': '1.8',
            'Debt_in_millions': '110',
            'Debt_to_Equity_Ratio': '0.25',
            'EBITDA_Margin_%': '18.75',
            'EBITDA_in_millions': '150',
            'Enterprise_Value_in_millions': '2100',
            'Equity_in_millions': '400',
            'Market_Capitalization': '2000',
            'Net_Income_in_millions': '40',
            'Number_of_Employees': '2000',
            'P_E_Ratio': '20',
            'ROA_Return_on_Assets_%': '6.5',
            'ROE_Return_on_Equity_%': '10',
            'Revenue_Growth_Rate_%': '8',
            'Revenue_in_millions': '800'
        })
    
    def test_when_get_data_file_not_found_then_throw(self):
        data = IPdfService(file_path = 'techcorp')
        with self.assertRaises(FileNotFoundError):
            data.get_data()
    
    def test_when_values_to_string_then_object_values_are_string(self):
        self.assertEqual(values_to_string({
            'Company Name': 'RetailCo',
            'Industry': 'Retail',
            'Market Capitalization': 2000,
            'Revenue (in millions)': 800,
            'EBITDA (in millions)': 150,
            'Net Income (in millions)': 40,
            'Debt (in millions)': 110,
            'Equity (in millions)': 400,
            'Enterprise Value (in millions)': 2100,
            'P/E Ratio': 20,
            'Revenue Growth Rate (%)': 8,
            'EBITDA Margin (%)': 18.75,
            'ROE (Return on Equity) (%)': 10,
            'ROA (Return on Assets) (%)': 6.5,
            'Current Ratio': 1.8,
            'Debt to Equity Ratio': 0.25,
            'Location': 'Chicago, IL',
            'CEO': 'Bob Johnson',
            'Number of Employees': 2000
        }), {
            'Company_Name': 'RetailCo',
            'Current_Ratio': '1.8',
            'Debt_in_millions': '110',
            'Debt_to_Equity_Ratio': '0.25',
            'EBITDA_Margin_%': '18.75',
            'EBITDA_in_millions': '150',
            'Enterprise_Value_in_millions': '2100',
            'Equity_in_millions': '400',
            'Market_Capitalization': '2000',
            'Net_Income_in_millions': '40',
            'Number_of_Employees': '2000',
            'P_E_Ratio': '20',
            'ROA_Return_on_Assets_%': '6.5',
            'ROE_Return_on_Equity_%': '10',
            'Revenue_Growth_Rate_%': '8',
            'Revenue_in_millions': '800'
        })
    
    def test_when_convert_obj_to_dict_then_value_is_dict(self):
        data = convert_obj_to_dict(self.expectedObj)
        self.assertEqual(type(data), dict)

    def test_when_get_property_name_then_return_property(self):
        content = '"Number of Employees": "2000"'
        self.assertEqual(get_property_name(content), 'Number of Employees')
    
    def test_when_prepare_key_then_key_is_clean(self):
        self.assertEqual(prepare_key("Company Name"), "Company_Name")
        self.assertEqual(prepare_key("EBITDA (in millions)"), "EBITDA_in_millions")
        self.assertEqual(prepare_key("P/E Ratio"), "P_E_Ratio")
    
    def test_when_get_diff_then_return_difference_objects(self):
        diff = IDiffLib({ 'id': '1', 'test': '2'}, { 'id': '2', 'test': 2, 'location': 'Italy'}).get_diff()
        self.assertEqual(diff, ['id', 'location', 'test'])

if __name__ == '__main__':
    unittest.main()
