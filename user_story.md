### User Stories

1. **As a Data Engineer**,  
I want to test and time the performance of the extraction process from the raw insurance dataset,  
so that I can ensure the pipeline is efficient.

2. **As a Data Engineer**,  
I want to transform the raw insurance dataset by cleaning numeric values, encoding categorical variables, and handling missing data,  
so that the dataset is standardised, structured, and ready for statistical analysis, predictive modelling, and visualisation.

3. **As a Data Engineer**,  
I want to load the transformed dataset into a database of my choice using env.test and .env.dev configurations,  
so that I can query and validate the data in a reproducible environment.

4. **As an Analyst**,  
I want to visualise correlations and trends in the insurance data through the Streamlit dashboard,  
so that I can explore how demographic and lifestyle factors influence insurance costs interactively.

5. **As a Developer**,  
I want to run unit, integration, and component tests across the ETL pipeline and dashboard,  
so that I can verify correctness, catch issues early, and ensure the system remains reliable.

---

# Plan / Checklist

---

### **Data Extraction**
- [ ] Raw insurance dataset is successfully extracted  
- [ ] Extraction time is logged  
- [ ] Extraction completes in under X seconds  
- [ ] Errors during extraction are logged and handled  
- [ ] Data is stored in a Pandas DataFrame  
- [ ] Unit tests validate extraction logic  

---

### **Data Transformation**
- [ ] Numeric columns cleaned and normalised  
- [ ] Categorical variables encoded consistently  
- [ ] Missing values removed  
- [ ] Outliers identified and handled  
- [ ] Final processed dataset is saved  
- [ ] Transformation steps are logged  
- [ ] Unit + integration tests validate transformations  

---

### **Data Loading**
- [ ] .env.test and .env.dev configured  
- [ ] Load function writes data into database  
- [ ] Schema is consistent and documented  
- [ ] Load failures are logged  
- [ ] Data retrieval is tested and verified  

---

### **Visualisation**
- [ ] Streamlit dashboard runs using **run_app** in terminal  
- [ ] Correlation interactive graph displayed  
- [ ] Interactive updates work smoothly  
- [ ] Dashboard reads only the processed dataset  

---

### **Testing & Validation**
- [ ] Unit tests for extraction  
- [ ] Unit tests for transformation  
- [ ] Unit tests for load  
- [ ] Integration tests for ETL end-to-end  
- [ ] Component tests for visualisation/dashboard  
- [ ] **run_tests** command executes all tests  
- [ ] Achieve 90%+ coverage (optional)

---