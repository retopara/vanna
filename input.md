# Input
## Model Elements
### Periods
#### PeriodName
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Cannot be empty, Period Name must be unique
	* Indicates the name of the Period, which can be referenced in the policy and Constraint tables
	* Must contain END, and the corresponding Start Date indicates the model End Date.
#### StartDate
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Cannot be empty,no default value
	* Represents the start time of the Period
	* The model end date requires adding a new row, with PeriodName as END, the StartTime of END period must be later than all StartTime of other period .
#### Notes
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty,no default value
	* Enter optional descriptive notes about the period. The "Notes" field  is not a mandatory field.

_ _ _

### Products
#### ProductName
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Cannot be empty,Product Name must be unique
	* Indicates the code or abbreviation of the Product
	* Must be called in the model's Customer orders,sourcing policy,transportation policy,and inventory policy,and can also be referenced in Constraints
	* The company's SKU code can be used directly,or it can be reclassified or clustered based on the model's requirements,taking into account the Product's physical properties,value,demand characteristics,supply characteristics,etc.
#### Value
* **Applicable Algorithms**: NO, SIM, SSO, TO, FA

* **Description**:
	* Can be empty, default value is 0, but in the safety stock optimization model, it is a necessary input element.
	* Represents the currency value of the unit Product.
	* Used to calculate inventory holding costs,reflected in the total inventory holding costs in the network summary output table: Inventory holding cost = Average inventory \* ProductValue \* Inventory holding cost rate% \* time in stock.
	* Product value in the inventory policy takes precedence over the value in the Product table.
	* If the inventory holding cost rate% is filled in the inventory policy, it will use the inventory holding cost rate% in the inventory policy, otherwise, the inventory holding cost rate% in the model settings will be used.
#### Price
* **Applicable Algorithms**: NO, SIM, SSO, TO, FA

* **Description**:
	* Can be empty,the default value is 0
	* Indicates the selling price of a unit Product
	* Statistics used to calculate revenue and profit:   * Revenue = Price\*Product demand quantity (Customer order table)
	* Profit = Revenue - Cost
	* If the unit price is specified on the Customer order table,the price in the Customer order table will override the price in the Product table,otherwise,the price in the Product table is used to calculate revenue by default.
#### Volume
* **Applicable Algorithms**: NO, SIM, OA, TO, FA

* **Description**:
	* Can be empty,the default value is 1,there is no default unit.Each model needs to keep the unit consistent
	* Indicates the Volume of the unit Product
	* Used for flow constraint or transportation cost calculation based on Volume.
#### Weight
* **Applicable Algorithms**: NO, SIM, OA, TO, FA

* **Description**:
	* Can be empty,default value is 1,no default unit,each model needs to keep the unit consistent
	* Indicates the Weight of the unit Product
	* Used for flow Constraint or transportation cost calculation based on Weight.
#### StartDate
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates the Start Date of the Product
	* Used to consider the age of the Product during demand analysis. The Start Date is only applicable when using the demand series as the propagation method
	* If the Product has a Start/End Date,and the resulting Product lifespan falls within the model time frame,then the Product lifespan is used as the Period length when calculating safety stock costs. If the Product lifespan exceeds the model time frame,the regular Period length value will be used.
#### EndDate
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates the End Date of the Product
	* Used to consider the Product age when performing demand analysis. End Date is only applicable when using Demand Series as the propagation method.   
	* If the Start/End Date is populated in the Product,and the resulting Product life is within the model time range,the Product life is used as the Period length when calculating safety stock costs. If the Product life exceeds the model time range,the regular Period length value is used.
#### ShelfLife
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,no default value,input must be a non-negative integer
	* Indicates the maximum number of days Product can meet demand or be used for production.
	* Used to limit how far in advance a Product can be produced
	* As a Product moves through the supply chain,its relative age is tracked and compared to Shelf Life. For example,if your model uses a monthly period and a Product Shelf Life of approximately 60 days (2 months),define Shelf Life as 60. A Shelf Life of 0 is considered invalid. If you use 0,the solver will consider there to be no Shelf Life (similar to using empty: that is,the Product will never expire)
#### ProductFamily
* **Applicable Algorithms**: NO, SIM, SSO, GF, TO, FA

* **Description**:
	* The "Product Family" field is used to describe the business category to which a product belongs.
	* It does not directly participate in calculations but is used to enhance the analysis dimension of the output tables.
#### Status
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Cannot be empty. Value can be selected from a dropdown list. Options: Include/Exclude. Default value: Include. 
	* Used to specify whether the product is involved in model optimization: 
	  * Include: Product is involved in model calculations 
	  * Exclude: Product is not involved in model calculations, and policies related to this product, such as inventory, sourcing, and product-specific transportation strategies and processes, will not be constructed. Use 'Exclude' if products are expired.
#### Notes
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the Product,which does not participate in model calculation.
#### Custom1
* **Applicable Algorithms**: NO, SIM, SSO, GF, TO, FA

* **Description**:
	* Can be empty,no default value
	* Represents any other custom information about the Product,which is easy to understand and filter,and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO, SIM, SSO, GF, TO, FA

* **Description**:
	* Can be empty,no default value
	* Represents any other custom information about the Product,which is easy to understand and filter,and does not participate in model calculation.

_ _ _

### ProductsMultiPeriod
#### PeriodName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Periods defined in the Period table and the groups they form (the group type must be Individual)
	* Indicates the Period in which all attributes of the Product are effective.
#### ProductName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the code or abbreviation of the Product.
#### Price
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,the default value is 0
	* Indicates the revenue generated by selling units of Product during the Period
	* Statistics used to calculate revenue and profit:   
	  * Revenue = Price\*Product demand quantity (Customer order table)
	  * Profit = Revenue - Cost
	* If the unit price is specified on the Customer order table,the price in the Customer order table will override the price in the Product table,otherwise,the price in the Product table is used to calculate the revenue by default.
#### Value
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,the default value is 0,but in the safety stock optimization model,it is a necessary input element
	* Represents the monetary value of the unit Product in the Period
	* Is the basis for calculating the inventory holding cost,which is reflected in the total inventory holding cost in the network summary output table:   * Inventory holding cost = average inventory \* Product value \* inventory holding cost rate % \* in-stock time
	* The Product value in the inventory policy takes precedence over the value in the Product table
	* If the inventory holding cost rate % in the inventory policy is filled,the inventory holding cost rate % in the inventory policy will be used. Otherwise,the inventory holding cost rate % in the model settings will be used.
#### Status
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can not be empty, input as optional value, default value is Include, options are Include, Exclude
	* Used to specify whether the product in the Period participates in model optimization:
	   * Include: Product participates in model calculation
	   * Exclude: Product does not participate in model calculation, and policies using this Product will not be built, including inventory, sourcing, product-specific transportation policies and processes. Select Exclude when the product is expired or when doing greenfield analysis for specific products.

_ _ _

### Sites
#### SiteName
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Cannot be empty,Site Name must be unique
	* Indicates the abbreviation or code of the supply chain network node,including the factory that produces the product,the warehouse that stores the product,and the node that reflects the customer's needs. It can also include key nodes or virtual sites for transportation
	* Customer orders,sourcing policy,transportation policy,and inventory policy in the model must all be called,and can also be referenced in Constraints
	* Different types of nodes are recommended to be distinguished by prefixes. The network level is distinguished by Site Name to determine the network architecture. The prefix name represents the node type,and the prefix name indicates the physical location. Example: MFG*XYZ,DC*Mexico,CZ_Beijing,represents a three-level network (factory,warehouse,and customer). A model must include at least two types of sites: factory/warehouse and customer.
#### SiteType
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty,default value is ExistingFacility,options include ExistingFacility,PotentialFacility,Customer
	* Used to distinguish whether the site supplies/stores Product or receives demand:   * Existing Facility: Site currently existing in the supply network
	* Potential Facility: Site currently non-existent in the supply network,optimization candidate
	* Customer: Site used to carry Customer demand,no inventory,cannot produce Product or transfer Product to other Sites.
	* Together with SiteStatus,it affects whether the site is covered during model optimization (see SiteStatus for details).
#### ReviewSchedule
* **Applicable Algorithms**: SIM

* **Description**:
	* Can be empty,no default value
	* Indicates how often the order is checked before it is shipped out. Orders that are longer than the current check period will not be shipped out.
#### FixedOperatingCost
* **Applicable Algorithms**: NO, OA

* **Description**:
	* Can be empty, default value is 0.
	* Indicates the fixed operating cost of the Site in the planning period, including manpower and site daily maintenance costs, etc., reflected in the total operating cost in the Network Summary output table
	* There are two ways to enter: fixed value and step value
	* Fixed value, e.g., $300000 means that the total operating cost of the Site during the modeling Period is $300000.
	* It can also be a tiered cost corresponding to the output quantity (outbound volume), with the input format being (cost1,output limit1),…,(costn,output limitn), e.g.,(300000,2000),(500000,4000),i.e.,during the modeling Period:
	* When 0\<=output volume\<=2000,the total operating cost is $300000
	* When 2000\<=output volume\<=4000,the total operating cost is $500000
	* Meanwhile, this Column limits the maximum processing capacity of the Site, i.e., during the modeling Period,the maximum output volume is 4000
	* If there is no upper limit on processing capacity, the last tier can be input as (9999999,99999)
	* The output volume basis and cost units can be customized,with the output volume basis unit defaulting to Quantity, maintaining consistency within a each model.
#### FixedStartupCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is 0.
	* Represents the one-time start-up cost for activating a Site. For multi-period models, this cost is only calculated once. It is reflected in the total start-up cost in the Network Summary output table
	* Similar to fixed operating costs, there are two input methods: fixed value and tiered value. The input format can refer to the fixed operating costs but cannot be used to limit the maximum processing capacity of the Site.
	* The output base units can be customized. The default output base unit is Quantity. Within each model, UOM should maintain consistent.
	* In network optimization, relating to defined Site Type, if Site Type is PotentialFacility or Consider, this start-up cost value is used as the basis for determining whether to select for start-up.
#### ThroughputBasis
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is Quantity,options include Quantity,Weight,Volume
	* Used to define the output measure of unit (outbound quantity or throughput)  for fixed operation and startup cost calculation.
#### FixedClosingCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is 0.
	* Indicates the one-time cost of closing an existing Site, reflected in the total closure cost in the Network Summary output table. 
	* In network optimization, relating to defined Site type, if it is ExistingFacility or Consider, this closure cost value take effect if the model decide to close the facility.
	* Similar to the fixed startup costs, a Site can only be opened and closed once in the model.
#### FixedCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 0.0
	* Indicates the carbon emissions of the fixed operation of the Site in the planning period,such as water and electricity consumption
	* There are two ways to enter. One is a fixed value. For example,300000 means that the total fixed carbon emissions of the Site in the model period is 300000 tons. You can also enter a step value. The input method is the same as the fixed operating cost
	* The output basis and carbon emission unit can be customized. The carbon emission basis unit defaults to Quantity,and each model must be consistent
	* Reflected in the carbon emissions in the network optimization summary output table
#### Co2Basis
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Quantity
	* Drop-down box options are Quantity,Volume,Weight
	* Used to set the basis for fixed carbon emissions
#### ExpansionOnly
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is False
	* If False is selected,the throughput level of the site can fluctuate in different periods
	* If True is selected,it means that the throughput level of the current period can only be maintained or increased to a higher level in the following periods. For example,under the optimization scenario,if the optimization status of a site is "Open at Level 2" in Period*001,there will be no optimization status "Open at Level 1" in the following periods Period*002,003... The throughput level here is the level of the output level defined by the fixed operating cost where the actual throughput falls.
#### Address
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty,no default value
	* Indicates detailed address information of the Site.
#### Zipcode
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty, no default value
	* Indicates the postal code of the site's address.
#### City
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty,no default value
	* Indicates the city where the site is located, which is the smallest unit of structured address
	* Country, state, and city cannot be empty at the same time. It is best to use English names so that geocoding tools can convert and obtain longitude and latitude. It is recommended to calculate longitude and latitude at the smallest address level. If the detailed address cannot be obtained, the geocodeing tool will use the provincial capital, metropolis, or geographic center of the country or city.
#### Province
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty,no default value
	* Indicates the state/province where the site is located
	* Applies to the scenario as same as City.
#### Country
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty, no default value
	* Indicates the country where the site is located
	* Same as the 'City' field.
#### Latitude
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty,no default value
	* Indicates the latitude of the geographical location of the Site,used to calculate the distance and map display of each Site.
	* Can be entered directly or obtained through Geocoding. For the city level,the latitude of the city government is generally used. For the province level,the center of the provincial capital is generally used. Any location has a corresponding specific latitude and longitude value. - There is no clear requirement for retaining decimals. It is recommended to retain 4 digits. The more decimal places provided,the more accurate the address information will be.
	* Use degree format,the latitude range is -90° \~90° (that is,90°S south latitude to 90°S north latitude). When the latitude format is degrees-minutes-seconds,it needs to be converted to degrees.
	* Conversion formula: Latitude = degrees + minutes/60 + seconds/3600
	* For example: Latitude 39°20'43" = 39+20/60+43/3600 = 39.3453
#### Longitude
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty,no default value
	* Indicates the longitude of the geographical location of the Site,used to calculate the distance and map display of each Site.   
	* Can be directly entered or obtained through Geocoding. For the city level,the longitude of the city government is generally used. For the province level,the center of the provincial capital is generally used. Any location has a corresponding specific longitude and latitude value. There is no clear requirement for retaining decimals. It is recommended to retain 4 digits. The more decimal places provided,the more accurate the address information will be.
	* Use degree format,the longitude range is -180° \~180° (that is,180°E west longitude to 180°S east longitude). When the longitude format is degrees-minutes-seconds,it needs to be converted to degrees
	* Conversion formula: longitude = degrees + minutes/60 + seconds/3600  * Longitude 120°20'43”=120+20/60+43/3600=120.3453
#### SiteFamily
* **Applicable Algorithms**: NO, SIM, SSO, GF, FA

* **Description**:
	* The Site family field is used to describe the business category to which the Site belongs.
	* Site Family does not directly participates in the model calculation, but is used to increase the analysis dimension for the output tables.
#### VariableServiceTimeBasis
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, the default value is Weight, other options include Volume and Quantity.
	* Defines the calculation basis of the variable service time required for loading and unloading operation of the site
#### MandatoryRoutingSequence
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is Not required,and the options include First Pickup (first stop pickup,that is,empty truck is required to enter),Last Pickup (last stop pickup),First Delivery (first stop delivery),Last Delivery (last stop delivery,that is,no other site goods are allowed to be on the truck when delivering)
	* Used to constrain the order of Sites in Asset Tour
	* Not effective yet.
#### NumberOfDockDoors
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value
	* Describes the number of platforms owned by the Site,that is,the maximum value of the Asset Id that can be loaded and unloaded at the same time
	* Not effective yet.
#### Status
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty,default value is Include,options include Include,Exclude,and Consider
	* Used to specify whether the site participates in model optimization:   
	  * Include: Participate in model calculation   
	  * Exclude: Do not participate in model calculation,no policy will be built to use this site,including inventory,sourcing,site-specific transportation policy and process.   
	  * Consider: When optimizing,the Site Type is different,driven by cost optimization,and the decision SiteStatus can be turned on or off
#### Notes
* **Applicable Algorithms**: NO, SIM, SSO, GF, OA, TO, FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the Site,which does not participate in model calculations.
#### Custom1
* **Applicable Algorithms**: NO, SIM, SSO, GF, TO, FA

* **Description**:
	* Can be empty,no default value
	* Represents any other custom information about the Site,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO, SIM, SSO, GF, TO, FA

* **Description**:
	* Can be empty,no default value
	* Represents any other custom information about the Site,which is convenient for understanding and filtering and does not participate in model calculation.
#### DockDoorResetTime
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value
	* Indicates the interval time for switching to use Asset Id on the Site platform,in minutes,that is,how long after the previous vehicle finishes the operation and leaves the platform,the next vehicle can enter the platform and start the operation.
	* Not effective yet.
#### FixedServiceTimeLoad
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 0
	* Indicates the fixed service time required for the site in the loading operation,such as platform preparation time,etc.,in minutes.
#### FixedServiceTimeUnload
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 0
	* Indicates the fixed service time required for the site in the unloading operation,such as platform preparation time,etc.,in minutes.
#### FixedServiceTime
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 0
	* Indicates the fixed service time required for the loading and unloading operations of the Site (after a single arrival and before the departure of any Asset Id),such as security inspection,appointment registration time,etc.,in minutes. The definition of service includes loading and unloading,and the definition of service time includes fixed and variable parts. Service time can be set through the three dimensions of order,asset,and site (i.e. the corresponding input table). Taking Order 1 of unloading from Asset A to Site A as an example,unloading time = fixed service time (SiteA+Asset A+Order 1) + fixed unloading time (SiteA+Asset A+Order 1) + variable unloading time (SiteA+Asset A+Order 1).
#### VariableServiceTimeBasis
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is Quantity,options include Quantity,Weight,Volume
	* Defines the calculation basis for Variable Loading/Unloading Time at the Site
#### VariableServiceTimeLoad
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 0
	* Indicates the variable service time required for the site in the loading operation,such as handling and loading time,etc.,in minutes per unit (Weight-kilograms,Volume-cubic meters,quantity-pieces). Assuming that the fixed service time of a site is 10 minutes,the variable loading time is 2 minutes,and the variable loading and unloading basis is Volume (Volume),then for an order with a volume of 5 square meters,the total loading time corresponding to the order is 10+5*2=20 minutes.
#### VariableServiceTimeUnload
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 0
	* Indicates the variable service time required for the unloading operation of the site,such as the handling and unloading time,etc.,in minutes per unit (Weight-kilograms,Volume-cubic meters,quantity-pieces). Assuming that the fixed service time of a site is 10 minutes,the variable unloading time is 2 minutes,and the variable loading and unloading basis is quantity (Quantity),then for an order of 5 pieces,the total loading time corresponding to the order is 10+5*2=20 minutes.

_ _ _

### SitesMultiPeriod
#### PeriodName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Periods defined in the Period table and the groups they consist of (the group type must be Individual)
	* Indicates the Period in which all attributes of the Site are effective.
#### SiteName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Sites defined in the Site table and their groups (the group type must be Individual)
	* Indicates the abbreviation or code of the supply chain network node.
#### FixedOperatingCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 0
	* Indicates the fixed operating cost of the Site during the Period,including manpower and daily site maintenance costs,reflected in the total operating cost in the network summary output table
	* The entry method is the same as the fixed operating cost method in the Site table.
#### FixedStartupCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 0
	* Indicates the one-time investment cost of newly building or enabling a new site in the Period. For a multi-Period model,this cost is calculated only once. Reflected in the total startup cost in the network summary output table
	* The entry method is the same as the fixed operating cost method in the Site table.
#### FixedClosingCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 0
	* Represents the one-time cost of closing an existing Site within the Period,reflected in the total closing cost in the network summary output table.
	  * Combined with the use of fixed startup costs,a Site can only be opened and closed once during the entire model period.
#### FixedCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Default is empty
	* Indicates the carbon emissions of the fixed operation of the Site within the planning period,such as water and electricity consumption
	* The input method is the same as the fixed carbon emissions of the Site table
	* Reflected in the carbon emissions of the network optimization summary output table
#### ReviewSchedule
* **Applicable Algorithms**: SIM

* **Description**:
	* Can be empty,no default value
	* Indicates how often the order is checked before it is shipped out. Orders that are longer than the current check period will not be shipped out.
#### Status
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can not be empty, input as optional value, default value is Include, options are Include, Exclude
	* Used to specify whether the site in the Period participates in model optimization:
	   * Include: Site participates in model calculation
	   * Exclude: Product does not participate in model calculation, and policies using this Product will not be built, including inventory, sourcing, site-specific transportation policies and processes.

_ _ _

### WorkCenters
#### SiteName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,no default value
	* Not required The unique drop-down box options are the Sites defined in the Site table (Site Type = ExistingFacility or PotentialFacility) and the groups composed of Sites (the group type must be Individual),indicating the Site to which the production belongs.
#### WorkCenter
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,no default value
	* Must be unique
	* Indicates the abbreviation and code of the production workshop or production line in the factory,which needs to be called in the production process of the model and can also be referenced in the Constraint conditions
#### WorkCenterType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, the default value is ExistingWorkCenter
	* No need to be unique
	* Used to distinguish between existing and potential workcenters
#### ExpansionOnly
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is False, options include True and False
	* Set whether the throughput level of the work center can fluctuate in different periods or can only increase through the periods
#### FixedOperatingCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 0,no need to be unique
	* Indicates the fixed operating cost of the work center in the planning period,including manpower and daily site maintenance costs,reflected in the total operating cost in the network summary output table. If the fixed operating cost of the production workshop is included in the site cost,this field can be left blank.
#### FixedStartupCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 0
	* Indicates the one-time cost of building a new or newly enabled Site. For multi-Period models,this cost is calculated only once. Reflected in the total startup cost in the network summary output table
	* Its usage is the same as that in the Site table.
#### FixedClosingCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 0
	* Indicates the one-time cost of closing an existing Site,which is reflected in the total closure cost in the network summary output table.
#### FixedCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 0.0
	* Indicates the carbon emissions of fixed operations of the work center in the planning period,such as water and electricity consumption
	* There are two ways to enter. One is a fixed value. For example,300000 means that the Site is in the model period,and the total fixed carbon emissions are 300000 tons. You can also enter a step value. The input method is the same as the fixed operating cost
	* The output quantity basis and carbon emission unit can be customized. The carbon emission basis unit defaults to Quantity,and each model must be consistent
	* Reflected in the carbon emissions in the network optimization summary output table
#### Co2Basis
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Quantity, options are Quantity, Hour, Volume, Weight
	* Defines the calculation basis for Fixed CO2 emissions
#### CostBasis
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Quantity,no need to be unique
	Used to define the output unit of fixed operation and startup costs.
#### Status
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty
	* the default value is Include
	* no need to be unique 
	* used to specify whether the work center participates in model optimization
#### Notes
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the work center,which does not participate in model calculations.

_ _ _

### WorkCentersMultiPeriod
#### PeriodName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Periods defined in the Period table and the groups they consist of (the group type must be Individual)
	* Indicates the Period in which all attributes of the work center are effective.
#### SiteName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Sites defined in the Site table (Site Type = ExistingFacility or PotentialFacility) and their groups (the group type must be Individual)
	* Indicates the Site to which the production belongs.
#### WorkCenter
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty, options are the work centers defined in Work Center table and their groups (the group type must be Individual)
	* Defines which Work Center shall be specially configured in different periods
#### FixedOperatingCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, the default value is 0.
	* Indicates the fixed operating cost of the work center in the Period, including manpower and daily maintenance costs, etc., reflected in the total operating cost in the Network Summary output table.
	* The usage method is the same as in the Site table.
#### FixedStartupCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 0.
	* Indicates the cost of one-time investment for new or reactivated Site within this Period. For multi-Period models,this cost is only calculated once. Reflected in the total startup cost in the Network Summary output table.
	* Its usage method is consistent with the usage method in the Site table.
#### FixedClosingCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is 0.
	* Indicates the one-time cost of closing the existing Site, reflected in the total closure cost in the Network Summary output table.
#### FixedCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Default is empty
	* Indicates the carbon emissions of the fixed operation of the Site within the planning period, such as energy consumption
	* The input method is the same as the fixed carbon emissions of the Site table
	* Reflected in the carbon emissions of the network optimization summary output table
#### Status
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the work center participates in model optimization within the Period:
	  * Include: Participate in model calculation
	  * Exclude: Do not participate in model calculation
#### Notes
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the work center within the Period,which does not participate in model calculation.

_ _ _

### BusinessHour
#### SiteName
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,select from the drop-down box. The drop-down box options are the Sites defined in the Site table and the groups consisting of some Sites (the group type must be Individual)
	* Identifies the Site Name or Site group for which the business hours are to be set.
#### MondayOpen
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 00:00:00
	* Indicates the Start Date of the Site's business hours every Monday. If a certain day (such as Sunday) is closed,fill in 23:59:00 for both the Start Date and End Date of that day. If there are multiple non-overlapping business periods on a certain day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),they should be filled in separate lines.
#### MondayClosed
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 23:59:00
	* Indicates the End Date of the Site's business hours on Mondays. If the site is closed on a certain day (such as Sunday),fill in 23:59:00 for both the Start Date and the End Date of that day.If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### TuesdayOpen
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 00:00:00
	* Indicates the Start Date of the Site's business hours on Tuesdays. If the site is closed on a certain day (such as Sunday),fill in 23:59:00 for both the Start Date and End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### TuesdayClosed
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 23:59:00
	* Indicates the End Date of the Site's business hours on Tuesdays. If the site is closed on a certain day (such as Sunday),fill in 23:59:00 for both the Start Date and the End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### WednesdayOpen
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 00:00:00
	* Indicates the Start Date of the Site's business hours on every Wednesday. If a certain day (such as Sunday) is closed,fill in 23:59:00 for both the Start Date and End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### WednesdayClosed
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 23:59:00
	* Indicates the End Date of the Site's business hours on Wednesdays. If the site is closed on a certain day (such as Sunday),fill in 23:59:00 for both the Start Date and the End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### ThursdayOpen
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 00:00:00
	* Indicates the Start Date of the Site's business hours on every Thursday. If a certain day (such as Sunday) is closed,fill in 23:59:00 for both the Start Date and End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### ThursdayClosed
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 23:59:00
	* Indicates the End Date of the Site's business hours on every Thursday. If a certain day (such as Sunday) is closed,fill in 23:59:00 for both the Start Date and the End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### FridayOpen
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 00:00:00
	* Indicates the Start Date of the Site's business hours every Friday. If a certain day (such as Sunday) is closed,fill in 23:59:00 for both the Start Date and End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### FridayClosed
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 23:59:00
	* Indicates the End Date of the Site's business hours on every Friday. If a certain day (such as Sunday) is closed,fill in 23:59:00 for both the Start Date and the End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### SaturdayOpen
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 00:00:00
	* Indicates the Start Date of the Site's business hours on every Saturday. If a certain day (such as Sunday) is closed,fill in 23:59:00 for both the Start Date and End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### SaturdayClosed
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 23:59:00
	* Indicates the End Date of the Site's business hours on every Saturday. If a certain day (such as Sunday) is closed,fill in 23:59:00 for both the Start Date and the End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### SundayOpen
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 00:00:00
	* Indicates the Start Date of the site's business hours every Sunday. If a certain day (such as Sunday) is closed,fill in 23:59:00 for both the Start Date and End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### SundayClosed
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 23:59:00
	* Indicates the End Date of the Site's business hours every Sunday. If a certain day (such as Sunday) is closed,fill in 23:59:00 for both the Start Date and End Date of that day. If there are multiple non-overlapping operational periods on a given day (such as 6:00:00-10:00:00 and 12:00:00-20:00:00),each period should be filled on separate rows.
#### Status
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,input is optional,default value is Include,optional options include Include,Exclude
	* Used to specify whether the asset participates in model optimization,Include means participating in model calculation,Exclude means not participating.

_ _ _

### WorkResource
#### WorkResource
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the work resource name must be unique
	* Defines the name of a work resource involved in the production process in one plant
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (the group type must be Individual)
	* Indicates the Site to which the work resource belongs.
#### FixedCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 0
	* Indicates the fixed cost of work resources in the planning period,such as the management cost of each staff member. Reflected in the total work resource cost in the network summary output table
	* Its usage is the same as the fixed operating cost in the Site table. There are two ways to enter: fixed value and step value.
#### HourlyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is 0.
	* Represents the hourly cost of work resources, typically used for workers' hourly wages. This cost reflects in the total Work Resource Cost in the Network Summary output table.
#### ExpansionOnly
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is False, options include True and False
	* Set whether the throughput level of the work resource can fluctuate in different periods or can only increase through the periods
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the work resource participates in model optimization within the Period:
	  * Include: Participate in model calculation
	  * Exclude: Do not participate in model calculation
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive description of the work resource,which does not participate in model calculations.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Represents any other custom information about the work resource,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Represents any other custom information about the work resource,which is convenient for understanding and filtering and does not participate in model calculation.

_ _ _

### WorkResourceMultiPeriod
#### WorkResource
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, options are the work resources defined in Work Resource table and their groups (the group type must be Individual)
	* Defines which Work Resource shall be specially configured in different periods
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (the group type must be Individual)
	* Indicates the Site to which the work resource belongs.
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the drop-down box options are the Periods defined in the Period table and the groups they consist of (the group type must be Individual)
	* Indicates the Period in which all attributes of the work resource are effective.
#### FixedCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 0
	* Indicates the fixed cost of work resources in different periods,such as the management cost of each staff member. Reflected in the total work resource cost in the network summary output table
	* Its usage is the same as the fixed operating cost in the Site table. There are two ways to enter: fixed value and step value.
#### HourlyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is 0.
	* Indicates the hourly cost of work resources in different periods, usually used for workers' hourly wages. This cost reflects in the Total Work Resource Cost in the Network Summary output table.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the work resource participates in model optimization within the Period:   
	  * Include: Participate in model calculation   
	  * Exclude: Do not participate in model calculation
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the work resource,which does not participate in the model calculation. 

_ _ _

## Transaction & Forecast
### CustomerOrders
#### OrderId
* **Applicable Algorithms**: SIM, FA

* **Description**:
	* Can be empty,no default value
	* Indicates Shipment number,you can directly enter the Shipment number from the enterprise management system.
#### OrderlineId
* **Applicable Algorithms**: SIM, FA

* **Description**:
	* Can be empty,no default value
	* Indicates the Shipment line number,you can directly enter the Shipment line number from the enterprise management system.
#### CustomerName
* **Applicable Algorithms**: NO, SIM, SSO, GF, FA

* **Description**:
	* Cannot be empty,the drop-down box options are Customer defined in the Site table (Site Type=Customer) and groups composed of Customers (the group type must be Individual)
	* Indicates the Customer name or Customer group in demand.
#### ProductName
* **Applicable Algorithms**: NO, SIM, SSO, GF, FA

* **Description**:
	* Cannot be empty,the drop-down box options are the products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the Product or Product group that has Customer demand.
#### OrderDate
* **Applicable Algorithms**: NO, SIM, SSO, GF, FA

* **Description**:
	* Cannot be empty
	* No default value, input value must be within the model time
	* Defines the date when the order must be fulfilled.
#### Quantity
* **Applicable Algorithms**: NO, SIM, SSO, GF, FA

* **Description**:
	* Cannot be empty,can be an integer or decimal,unit can be customized,but must remain consistent
	* Indicates the quantity of the product that the Customer demands.
#### UnitPrice
* **Applicable Algorithms**: NO, SIM, FA

* **Description**:
	* Can be empty,no default value
	* Indicates the unit price of this ShipmentProduct. When there are multiple entries in the Customer Orders table for the same Customer-Product combination during the same period,and one of them has entered a unit Price,this Price will be used to overwrite the unit price of all Shipments for that CustomerProduct combination during the period. If multiple Shipments have different unit prices,a weighted average unit price based on quantity and order frequency will be used to overwrite the unit price of all Shipments for that CustomerProduct combination during the period.
#### MaxDeliveryTime
* **Applicable Algorithms**: SIM, FA

* **Description**:
	* Can be empty, no default value,default unit is day
	* Specifies the maximum time allowed for delivery after the customer places the order.
	* If the order is completed immediately after it is placed, leave it blank or enter 0,if it arrives 1 day later,enter 1.
#### Status
* **Applicable Algorithms**: NO, SIM, SSO, GF, FA

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the Customer order participates in model optimization:   
	  * Include: participate in model calculation   
	  * Exclude: do not participate in model calculation
#### Notes
* **Applicable Algorithms**: NO, SIM, SSO, GF, FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of Customer requirements,not involved in model calculation.
#### Custom1
* **Applicable Algorithms**: NO, SIM, SSO, GF, FA

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about Customer requirements,which is easy to understand and filter,and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO, SIM, SSO, GF, FA

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about Customer requirements,which is easy to understand and filter,and does not participate in model calculation.
#### DaysAllowedDelay
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, no default value
	* Enter the number of days that the order can be delayed for fulfillment. For example, if the order can be fulfilled within 15 days of the order date, enter 15.
#### UnitLostSalesPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, no default value
	* The penalty cost directly incurred per unit due to unfulfilled customer orders caused by stockouts.
#### MinRatio
* **Applicable Algorithms**: NO

* **Description**:
	* The default value is 0,which means that the entire order quantity is met.
	* The input must be a decimal,with a maximum value of 1.0.
	* If this filed is used,then the minimum satisfaction ratio for the order is order quantity * minimum satisfaction ratio
#### UnitEarlyPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, no default value
	* Defines the cost incurred per unit for early delivery of products.
#### OrderQuantityStd
* **Applicable Algorithms**: NO

* **Description**:
	 * Can be empty. No default value. 
	* For customer orders with fluctuations in order quantity, this field can be used to input the degree of fluctuation into the model to more accurately reflect changes in order quantity.                                                                                                                                                                                
#### DaysAllowedEarly
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, no default
	* Enter the number of days in advance that an order can be fulfilled. For example, if an order can be delivered 15 days before the order date, enter 15.
#### UnitDelayPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Defines the cost per unit of Product incurred when an order is delayed

_ _ _

### CustomerForecast
#### PeriodName
* **Applicable Algorithms**: NO, SSO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Period defined in the Period table
	* Indicates the applicable Period of the forecast data.
#### CustomerName
* **Applicable Algorithms**: NO, SSO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are Customer defined in the Site table (Site Type=Customer) and groups composed of Customers (the group type must be Individual)
	* Indicates the Customer name or Customer group in demand.
#### ProductName
* **Applicable Algorithms**: NO, SSO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the Product or Product group that has Customer demand.
#### ForecastNzMean
* **Applicable Algorithms**: NO, SSO, SIM

* **Description**:
	* Can be empty, no default value.
	* Used for demand classification, indicating the average daily non-zero demand within the Period.
#### ForecastNzStd
* **Applicable Algorithms**: NO, SSO, SIM

* **Description**:
	* Can be empty,no default value
	* Used for demand classification,indicating the standard deviation of the non-zero daily average demand predicted within the Period.
#### ForecastDemandInterval
* **Applicable Algorithms**: NO, SSO, SIM

* **Description**:
	* Can be empty
	* No default value
	* Used for demand classification, defines the average interval days of demand forecasted within the Period.
#### ForecastMean
* **Applicable Algorithms**: NO, SSO, SIM

* **Description**:
	* Cannot be empty, no default value.
	* Used for demand propagation and demand classification, which indicates the average daily demand forecast within the Period.
#### ForecastError
* **Applicable Algorithms**: NO, SSO, SIM

* **Description**:
	* Cannot be empty,no default value
	* Used for demand propagation and demand classification,indicating the forecast error (RMSE) of the average daily demand predicted within the Period.
#### Status
* **Applicable Algorithms**: NO, SSO, SIM

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether Customer orders participate in model optimization

_ _ _

## Transaction & Forcast
### Shipments
#### OrderId
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Cannot be empty, no default value
	* Indicates the order number.  Can directly enter the order number in the enterprise management (ERP) system.
#### SourceName
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Cannot be empty,select from the drop-down box,the drop-down box options are non-Customer defined in the Site table (Site Type=ExistingFacility,PotentialFacility)
	* Indicates the starting point of the transport order,that is,the location where the order loading operation is performed.
#### CustomerName
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Cannot be empty,select from the drop-down box,the drop-down box options are the Sites defined in the Site table (Site Type = ExistingFacility,PotentialFacility,Customer)
	* Indicates the destination of the transport order,that is,the location where the order unloading operation is performed.
#### ProductName
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Cannot be empty,the drop-down box options are the products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the Product or Product group that has Customer demand.
#### Quantity
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Cannot be empty,no default value,it is recommended to fill in a positive integer (filling in a decimal will not result in an error,but it will affect the model calculation and output results),the unit can be customized,but model must be consistent
	* Indicates the number of Products shipped in the order.
#### OrderDate
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Cannot be empty
	* No default value, recommended to input the value within the Periods defined in the Period table.
	* Defines the date when the order is placed or the order information is entered into the system.
#### Weight
* **Applicable Algorithms**: OA, TO

* **Description**:
	* can be empty. 
	* No default value. If the field is empty, the value of order quantity and the unit product Weight from the Product table will be used to calculate the total Weight of the order.
	* indicates the total Weight of the order.
	* It is recommended to fill in a positive integer (filling in a decimal will not cause an error,but it will affect the model calculation and output results).
#### Volume
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Indicates the total volume of the shipment order
	* Can be empty. If the field is empty, the unit product volume in the Product table * order quantity will be calculated to obtain the total Volume of the shipment, no default value, volume unit is cubic meters by default, accurate to three decimal places (i.e.,accurate to deciliters,liters),can be customized to others,but a each model must remain consistent
#### EarliestPickupDate
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty
	* No default value, input value is recommended to be within the Periods defined in the Period table
	* Defines the earliest pick-up date at the pick-up point.
#### LatestPickupDate
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty
	* No default value. Input value is recommended to be within the Periods defined in the Period table. If the value exceeds the latest time of the Period,the latest time of the Period shall prevail.
	* Defines the latest pick-up date at the pick-up point. The latest pickup date should be later than the earliest pickup date.
#### EarliestDeliveryDate
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty
	* No default value,input value is recommended to be within the Period defined in the Period table
	* Indicates the earliest unloading date at the drop-off point.
#### LatestDeliveryDate
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty
	* No default value. Input value is recommended to be within the Periods defined in the Period table. If the value exceeds the latest time of the Period,the latest time of the Period shall prevail.
	* Defines the latest unloading date at the drop-off point. The latest delivery date should be later than the earliest delivery date.
#### Priority
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Cannot be empty,default value is 1
	* Currently not in function.
#### VariableServiceTimeBasis
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Cannot be empty,default value is Quantity, other options include Volume and Weight
	* Defines the calculation basis of the variable service time required for the loading and unloading operation for each shipments. 
	Note: In Hub Transportation Optimization scenario, the variable loading and unloading basis is effective for both inbound and outbound legs.
#### SubScenario
* **Applicable Algorithms**: TO

* **Description**:
	* Not required, can be empty
	* Used to specify the sub-scenario to which each shipment belongs. Note that shipment orders with empty values belong to the same scenario. For example, if "March 28", "March 29", and empty values are filled in the sub-scenario field, the algorithm will build three models to solve the shipment orders corresponding to "March 28", "March 29", and empty values, and add the sub-scenario name suffix to the original scenario name to differentiate them in the output.
#### Status
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the Customer order participates in model optimization,Include means participating in model calculation,Exclude means not participating.
#### Notes
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of Customer requirements,which is convenient for understanding and screening and does not participate in model calculation.
#### Custom1
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about Customer requirements,which is easy to understand and filter,and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about Customer requirements,which is easy to understand and filter,and does not participate in model calculation.
#### Volume
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty, no default value. The default unit of Volume is cubic meter, accurate to three decimal places (that is, accurate to cubic decimeter or liter). can be customized to other, but each model must be consistent
	* If the field is empty, the product name and quantity fields will be used, combined with the Volume of the Product in the Product table (Products - Volume) to calculate the total volume of the order
	* Indicates the total volume of the order.
#### FixedServiceTimeUnload
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty,no default value
	* Indicates the fixed service time required for the order in the unloading operation,such as the time for unpacking and unpalletizing the order,in minutes. Note: In the Hub function,the fixed unloading time is effective for both the trunk and branch lane leg.
#### FixedServiceTimeLoad
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty,no default value
	* Indicates the fixed service time required for the order in the loading operation,such as the order packing and palletizing time,in minutes. Note: In the Hub function,the fixed loading time is effective for both the trunk and branch lane legs.
#### FixedServiceTime
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty,no default value
	* Indicates the fixed service time required for any loading and unloading operation of the order,such as order scanning and registration time,in minutes. The definition of service includes loading and unloading,while the definition of service time includes fixed and variable parts. Service time can be set through the three dimensions of order,asset,and site (i.e. the corresponding input table). Taking the unloading order 1 from Asset A to Site A as an example,unloading time = fixed service time (SiteA+Asset A+Order 1) + fixed unloading time (SiteA+Asset A+Order 1) + variable unloading time (SiteA+Asset A+Order 1). Note: In the Hub function,fixed service time is effective in both trunk and branch lane legs.
#### DirectShippingCost
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty, no default value
	* Indicates the cost of direct shipping for the order if not using the Asset specified by the model, such as less-than-truckload or express delivery. The model will decide whether to choose direct shipping based on total cost optimization. Generally, do not set the direct shipping cost to 0.
#### Weight
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty, no default value, it is recommended to fill in a positive integer (filling in a decimal will not result in an error, but it will affect the model calculation and output results), the default unit of Weight is kilograms, which can be customized to other units, but each model must be consistent
	* If the field is empty, the values of the Product Name and Quantity fields will be used, combined with the Weight (unit ProductWeight) of the Product in the Product table to calculate the total Weight of the order
	* Indicates the total Weight of the order.
#### Value
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty, default value is 0.
	* Indicates the currency value of the Shipment.
	* This field is the basis for calculating inventory holding costs, reflected in the total inventory holding costs in the Network Summary output table.
#### VariableServiceTimeUnload
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty,no default value
	* Indicates the variable service time required for the unloading operation of the order,such as the handling and unloading time of the order,in minutes per unit (Weight-kilograms,Volume-cubic meters,quantity-pieces). Assuming that the Weight of an order is 5000kg,the fixed service time is 10 minutes,the variable unloading time is 0.002 minutes,and the variable loading and unloading basis is Weight (Weight),then the total unloading time corresponding to the order is 10+5000*0.002=20 minutes. Note: In the Hub function,the variable unloading time is effective in both the trunk and the branch lane legs.
#### MaximumDealyInDays
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty, no default value
	* Indicates the number of days that the shippment can be delayed
#### DailyUnitHoldingCost
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty, no default value
	* Indicates that if the shipment is not dispatched on the same day, the cost required per unit per day while waiting for shipment
#### VariableServiceTimeLoad
* **Applicable Algorithms**: OA, TO

* **Description**:
	* Can be empty,no default value
	* Indicates the variable service time required for the loading operation of the order,such as the handling and loading time of the order,in minutes per unit (Weight-kg,Volume-cubic meters,quantity-pieces). Assuming that the volume of an order is 5 cubic meters,the fixed service time is 10 minutes,the variable loading time is 2 minutes,and the variable loading and unloading basis is Volume (Volume),then the total loading time corresponding to the order is 10+5*2=20 minutes. Note: In the Hub function,the variable loading time is effective in both the trunk and the branch lane legs.

_ _ _

## Production
### ProductionPolicies
#### SiteName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is \*Facility,the group type must be Individual)
	* Indicates the Site to which the production policy applies
#### ProductName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the product to which the production policy applies
#### FixedProductionTime
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,default value is 0.0
	* Defines the fixed number of days to produce the Product,regardless of the quantity produced.
#### FixedProductionTimeStd
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,default value is 0.0,default unit is day
	* Indicates the standard deviation of the fixed number of days to produce Product,regardless of the quantity produced.
#### UnitProductionTime
* **Applicable Algorithms**: SIM

* **Description**:
	* Can be empty,default value is 0.0
	* Indicates the time required to produce a unit of finished product,the unit is the specified time base.
#### TimeBasis
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,default value is Days, options include Days,Hours,Minutes,Seconds
	* Defines the calculation basis for Unit Production Time
#### FixedProductionCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.0.
	* Represents the fixed production cost for each batch of the Product production, regardless of the production quantity.
#### UnitProductionCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.0.
	* Indicates the unit cost of the certain finished product per production unit. A tiered cost editor can be used here to implement step costs under different production volumes.
#### UnitCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 0.0
	* Used to set the unit carbon emission value of Product production
	* Reflected in the carbon emission of the network optimization summary output table
#### DaysBetweenProduction
* **Applicable Algorithms**: NO, SSO

* **Description**:
	* Can be empty,default value is 0.0
	* Defines the number of days between two production operations occured at the production site. This field is used to calculate the Cycle Stock that the site should keep, which equals to the production volume divided by the how many times production occurred in that period.
	* For SSO,this field is used for demand transmission and safety stock optimization. For safety stock calculation,when the service type is defined as type 2 or type 3,this value is used to derive the minimum replenishment quantity.
#### MinimalOrderQuantity
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty, default value is 0.0, default unit is Quantity
	* Defines the minimum order quantity of production for each production policy, which is the order quantity used when calculating Cycle stock and for demand analysis and safety stock optimization. It is also the minimum production quantity limit.
#### OrderLotSize
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,the default value is 0.0,the default unit is Quantity
	* Defines the production batch size,and production must be carried out in integer multiples of the production batch.
#### Status
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,default value is Include,optional options include Include,Exclude
#### Notes
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about the production policy,which does not participate in model calculation.
#### Custom1
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the production policy,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the production policy,which is convenient for understanding and filtering and does not participate in model calculation.
#### EnforceProcessProduction
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is False
	* In the Site specified by this row,the specified Product must go through the corresponding production process defined in the "Production Process" table and the "Production Process Assignment" table to complete production,and cannot skip the production process to complete production directly based on the production policy.
#### EnforceBomProduction
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is False
	* In the Site specified by this row,the specified finished product/intermediate product must be produced through the corresponding materials and corresponding proportions defined in the "Bom" table and the "Bom Assignment" table,and cannot skip materials to complete production directly based on the production policy.
#### PolicyPriority
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 1
	* When duplicate values appear in this production policy (same Site,same Product),the production policy with the smaller number in this field will be used first
#### PolicyType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, the default value is "Make", options include Make,  ProductGlobelRatio, and ProductLocalRatio
	* Indicates the policy type of this production policy
#### PolicyParameter
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty
	* Default value is 100.0
	* When "ProductGlobalRatio" is selected as "Production Policy - Policy Type",the parameter defined in this field is the ratio of the product produced by the site specified in this row.
	* When "ProductLocalRatio" is selected as "Production Policy - Policy Type",the parameter defined in this field is the ratio of the product specified in this row to all products produced by the site.

_ _ _

### ProductionPoliciesMultiPeriod
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table
	* Indicates the Period to which the production policy applies.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is \*Facility,the group type must be Individual)
	* Indicates the Site to which the production policy applies.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the Product to which the production policy applies.
#### DaysBetweenProduction
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 0.0
	* Defines the number of days between productions at the production site in different periods.
#### UnitProductionCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is 0.0.
	* It indicates the unit cost of producing a single unit of finish goods in different periods. A tiered cost editor can be used to implement Step costs under different production volumes.
#### UnitCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Default is empty
	* Reflects the unit carbon emission value within the Period.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the production policy participates in model optimization:  
	  * Include: The production policy participates in model calculation
	  * Exclude: The production policy does not participate in model calculation and will not be used for production.
#### PolicyPriority
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 1
	* Indicates the modified value of the production policy priority in different periods. This value can be used to modify the policy priority field in the production policy table in a specific period.
#### PolicyParameter
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty
	* Default value is 100.0
	* When the policy type is selected

_ _ _

### BOM
#### BomName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty, no default value
	* Indicates the code or abbreviation of Bom
#### ProductName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the code or abbreviation of the component Product used in Bom. Eg Finished pure milk is made from Bom Product raw milk,producing a by-product Product milk powder. The Product Name in Bom only includes raw milk and milk powder,not finished pure milk.
#### Type
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty, the default value is Component. Options include Component and Byproduct.
#### Quantity
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,the default value is 1
	* Indicates the number of components or by-products required to produce the final product
#### UnitCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 0.0
	* Used to set the unit carbon emission value of Bom
	* Reflected in the carbon emission of the network optimization summary output table
#### Status
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,the default value is Include
#### Notes
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about Bom,which does not participate in model calculation.
#### Custom1
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about Bom,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about Bom,which is convenient for understanding and filtering and does not participate in model calculation.

_ _ _

### BOMAssignment
#### PeriodName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the Period to which the Bom match applies.
#### SiteName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the Site to which the Bom match applies.
#### ProductName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty, no default value
	* Please note that it should be distinguished from the Product in the **Bom** table. The Product in the **Bom assignment*
	* table indicates the Product generated by this Bom (the finished product corresponding to the Bom), and the Product in the **Bom** table indicates the Product that makes up the Bom (what input materials the Bom contains).
	* Eg Finished milk is made from the raw milk of Bom Product, so in the Bom assignment table, the Product can be named "FG_Finished milk"
#### BomName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty, no default value
	* Indicates the Bom that the Bom assignment applies to.
#### PolicyType
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* To be developed
	* Can be empty
	* Default value is Single, options include Single and Multiple
	* Used to specify the allocation policy used for Bom assignment
#### PolicyParameter
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,the default value is 0.0
	* Used to specify the proportion of Bom used based on the Site-Product combination. This parameter takes effect when the policy type is Multiple. The parameter range is 0-100. For example,25 means that when the Product is produced at the Site,25% of the output uses this Bom.
#### UnitBomCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.0.
	* Represents the unit cost generated in BOM Assigntment.
	* The unit BOM cost is reflected in the total production cost of the Network Optimization Summary output table and the BOM cost in the BOM Flow output table.
#### Status
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,the default value is Include,optional options include Include,Exclude
	* Used to specify whether Bom participates in model optimization
#### Notes
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about Bom assignment,which does not participate in model calculation.

_ _ _

### ProductionProcess
#### PeriodName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the default value is All_Periods
	* Indicates the Period to which the production process applies.
#### ProcessName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty, no default value
	* Process name must be unique
	* Indicates the code or abbreviation of the production process.
#### ProcessStep
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty, no default value
	* Process Step name does not need to be unique
	* Indicates the Process Step in the production process.
#### StepSequence
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty, default value is 1.0
	* Indicates the order of the Process Step of in the production process. "1" stands for the first step, "2" stands for the second step, etc.
#### WorkCenter
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,no default value, options are the work centers defined in Work Center table and their groups (the group type must be Individual)
	* Defines the work center on which the production process shall be conducted.
#### RoutingPolicy
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the default value is FirstStep
	* Defines the routing policy for each Production Process Step
#### VariableProcessCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.0.
	* Indicates the unit cost required to complete a production process.
#### VariableProcessCostBasis
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,default value is Quantity,options include Quantity,Volume,Weight
	* Defines the calculation basis for Variable Process Cost
#### OrderLotSize
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,default value is 0,default unit is Quantity
	* Defines the batch size for Process production,which needs to be produced in multiples of the order batch.
#### MinimalOrderQuantity
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,default value is 0,default unit is Quantity
	* Defines the minimum order quantity for Process production.
#### FixedLotSetupCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.
	* Indicates the fixed cost for each batch in Process production.
#### UnitProcessHour
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,default value is 0
	* Defines the number of hours required to produce a unit in the production process.
#### FixedProcessHour
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty. Default value is 0. 
	* Represents the hours required to complete the production process, independent of production volume.                                                                                                                                                                                                                                               
#### MoveHour
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty. Default value is 0. 
	* Represents the hours required to switch from this process to the next. 
	* For NO algorithm: Related to batch size. Calculates one changeover time per batch. If no batch size is set, it calculates one changeover time for each product produced in a cycle. 
	* For SIM algorithm: To be developed.                                                                      
#### ChangeoverHour
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty. Default value is 0. 
	* Represents the hours required to switch from this process step to the next. 
	* For NO algorithm: Related to batch size. Calculates one changeover time per batch. If no batch size is set, it calculates one changeover time for each product produced in a cycle. 
	* For SIM algorithm: To be developed.                                                                      
#### WorkResource
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty
	* No default value
	* Specify the resource used in the production process.
#### WorkResourceHour
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty. Default value is 0.0. 
	* Represents the hours consumed by resources in the production process to produce one unit of product.                                                                                                                                                                                                                                                          
#### Yield
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty
	* the default value is 1.0
	* Set the yield rate of the production process, usually a value between 0 and 1
#### UnitCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value 0.0
	* Used to set the unit carbon emission value of the production process
	* Reflected in the carbon emission of the network optimization summary output table.
#### Status
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,default value is Include,options include Include,Exclude
	* Used to specify whether the production process participates in model optimization
#### Notes
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the production process,which does not participate in model calculations.

_ _ _

### ProductionProcessAssignment
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is All_Periods,and the drop-down box options are the Periods defined in the Period table.
	* Indicates the Period applicable to the production process match.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is \*Facility)
	* Indicates the Site to which the production process matches.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the Product to which the production process matches.
#### ProcessName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, no default value, the drop-down box options are the production processes defined in the production process table
	* Indicates the production process that the assignment applies to.
#### PolicyType
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, the default value is SingleProcess, and the options include SingleProcess and MutipleProcess
	* Used to specify whether the production process participates in model optimization:   
	  * SingleProcess: Based on the Site-Product combination, only one production process can be used for production
	  * MutipleProcess: Based on the Site-Product combination, multiple production processes can be used for production.
#### PolicyParameter
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 100.0
	* Used to specify the proportion of production processes used based on the Site-Product combination. This parameter takes effect when the policy type is MultipleProcess. The parameter range is 0-100. For example,25 means that when the product is produced at the site,25% of the output uses this production process.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Include,optional options include Include,Exclude
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about production process assignment,which does not participate in model calculation.

_ _ _

### ProductionConstraints
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Expression Name is optional but must be unique. Expressions created by production constraints can be used in the following ways: 
	  1. Creating expression constraints by specifying an expression for the value of expression1 or expression2. This enables combining constraints
	  2. Creating expression-based costs by using a defined expression name in the Expression Cost table,enabling definition of fixed and variable costs resulting from the constraint.
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the Period to which the production limit applies.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the site to which the production Constraint applies.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the Product to which the production Constraint applies.
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin,Lots,FixedLots,Define
	* Used to specify the type of production Constraint:   
	* Min: The production volume must be greater than or equal to the constraint value
	* Max: The production volume must be less than or equal to the constraint value
	* Fixed: The production volume must be equal to the constraint value
	* CondMin: The production volume can be 0,if not 0,it must be greater than or equal to the constraint value
	* Lots: Define the batch size  (the actual quantity may not be an integer multiple of the batch),and the final calculated Lots quantity will be rounded up
	* FixedLots: Define the batch size (the actual quantity must be an integer multiple of the batch),if the actual quantity is not an integer multiple,the model will be infeasible
	* Define: Used to create an expression,no constraint value needs to be filled in
	* When Lots and FixedLots limit the batch quantity,the "Expression" field must be filled in,and the "Expression Constraint" table must be used for Constraint.
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the production volume limit. For example,the No. 2 production line of the ABC factory produces A Product. If the production volume is greater than 5 tons,it will be turned on,otherwise,it will be turned off. In this case,fill in CondMin for the Constraint type and 5 for the Constraint value.
#### CostBasis
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is Quantity,options include Quantity,Volume,Weight
	* basis used to specify production constraint value:   * Quantity: Quantity  * Volume: Volume  * Weight: Weight  * Units of each field in the model must be consistent (no default unit)
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive statement about production constraints,not involved in model calculation.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include. It is used to specify whether production Constraints participate in model optimization.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about production constraints,for easy understanding and filtering,not involved in model calculation.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about production constraints,for easy understanding and filtering,not involved in model calculation.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty
	* The default value is 1. It is used to set the penalty cost per unit when the soft constraint is not met.
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.

_ _ _

### ProductionProcessConstraints
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, no default value
	* This is a custom name for the production process constraint. Application scenarios include: 
	  1. Creating an expression Constraint Group by providing values for Expression 1 and Expression 2,
	  2. Creating an expression-based cost by using this value in the Expression field, enabling the definition of fixed and variable cost components resulting from the constraint
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table,or the Period group,* indicates the Period to which the production process Constraint applies,* can be a single Period,it can be an Individual Period group,representing the production process Constraint that exists in each Period,or it can be a SET Period group,representing the production process Constraint summarized by this Period group
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is \*Facility)
	* Indicates the starting site to which the production process Constraints apply
	* If the Individual group is selected,it represents the independent Constraints for each member in the group,and if the SET group is selected,it represents the process Constraints for the collective total of all the group members.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the products defined in the Product table and the groups they form
	* Indicates the product to which the production process Constraint applies
	* If the Individual group is selected,it represents the independent Constraint of each member in the group,and if the SET group is selected,it represents the process Constraint of the collective total of all the group members.
#### ProcessName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, no default value, the drop-down box options are the processes defined in the production process table and the groups they form,
	* indicates the process to which the production process Constraint applies,
	* If an Individual group is selected, it means that each individual member in the group has independent Constraints, and if a SET group is selected, it means the process Constraint  applies to the total value of the group members.
#### ProcessStep
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, no default value, the drop-down box option is the process step defined in the production process table,
	* indicates the process step of the production process to which the production process Constraint applies
#### WorkCenter
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* No default value
	* Options in the dropdown list are the work centers defined by the Work Center table and their composed groups
	* Defines the applicable work centers for the production process Constraints,
	  * If 'Individual' group is selected, the constraint will be applied respectively on each member of the individual group. 
	  * If 'Set' group is selected, the constraint will be applied collectively on the set group as a whole.
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value,
	* indicates the limited amount of the production quantity of the production process
#### CostBasis
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value,options include Hour,Quantity,Volume,Weight,Value,Price
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin,Lots,FixedLots,Define
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the production process Constraints participate in model optimization:
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of production process Constraints,not involved in model calculation.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 1
	* Indicates the penalty cost per unit for violating the production process constraint.
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.

_ _ _

## Sourcing
### SourcingPolicies
#### SourceName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is \*Facility,the group type must be Individual)
	* Indicates the starting point Site to which the sourcing policy applies.
#### SiteName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (the group type must be Individual)
	* Indicates the endpoint Site to which the sourcing policy applies.
#### ProductName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the Product to which the sourcing policy applies.
#### PolicyType
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty, default value is MultipleSource, options include MultipleSource, SingleSource, and Ratio
	* Used to specify which policy is used to satisfy the replenishment order of the Site-Product combination: 1. MultipleSource: Based on the Site-Product combination, there are multiple sites that can be used as the sourcing site 2. SingleSource: Based on the Site-Product combination, there is only one site avaliable at the sourcing site 3. Ratio: Based on the Site-Product combination, there are multiple sites that can be used as the sourcing site and allocated according to a fixed ratio
#### PolicyParameter
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,the default value is 100.0
	* Used to specify the ratio of the sourcing policy used based on the Site-Product-starting point combination. This parameter takes effect when the policy type is Ratio. The parameter range is 0-100. For example,25 means that when the Site needs to purchase the Product,25% of the purchase volume comes from the source.
#### FixedSourcingTime
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Cannot be empty,default value is 0.0
	* Indicates the number of days used for evaluation after the source Site receives the Order,regardless of the quantity purchased.
#### FixedSourcingTimeStd
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty,default value is 0.0
	* Indicates the standard deviation of the number of days used to review the order after it is received by the source site,regardless of the quantity purchased.
#### UnitSourcingTime
* **Applicable Algorithms**: SIM

* **Description**:
	* Can be empty,default value is 0.0.
	* Indicates the unit time spent at the source Site after receiving the order and before reviewing the order, measured in days.
#### FixedSourcingCost
* **Applicable Algorithms**: SIM

* **Description**:
	* Can be empty, default value is 0.0.
	* Indicates the fixed cost of purchasing the Product from this Site, regardless of the quantity purchased.
	* Enter the fixed sourcing cost in the sourcing policy, and IO will calculate replenishment quantity and cycle stock accordingly.
#### UnitSourcingCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.0.
	* Indicates the average cost of procuring the unit Product between SourceSite and SiteSite, usually including fees such as tariffs, rather than the actual transport cost of the Product. The stepped cost editor can be used to implement the Step costs under different procuring volume.
#### UnitCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 0.0
	* Used to set the unit carbon emission value of Product purchase
	* Reflected in the carbon emission of the network optimization summary output table
#### MinimalOrderQuantity
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,default value is 0.0
	* Indicates the minimum order quantity for sourcing, the order quantity used when calculating cycle stock, demand analysis and safety stock optimization.
#### MaxSourcingDistance
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty
	* default value is 0.0
	* Set the maximum distance for upstream sourcing selection.
#### OrderLotSize
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,default value is 0.0.
	* Indicates the sourcing batch size,sourcing must be in multiples of the order batch size.
#### Status
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the sourcing policy participates in model optimization:   
	  * Include: The sourcing policy participates in model calculation
	  * Exclude: The sourcing policy does not participate in model calculation and will not be used for sourcing.
#### Notes
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the sourcing policy,which is not involved in the model calculation.
#### Custom1
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the sourcing policy,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the sourcing policy,which is convenient for understanding and filtering and does not participate in model calculation.
#### PolicyPriority
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 1
	* When duplicate values appear in this sourcing policy (same Site,same Product),the sourcing policy with the smaller number in this field will be used first

_ _ _

### SourcingPoliciesMultiPeriod
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table
	* Indicates the Period applicable to the sourcing multi-Period policy
#### SourceName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is \*Facility,the group type must be Individual)
	* Indicates the starting point Site to which the sourcing multi-period policy applies.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (the group type must be Individual)
	* Indicates the end site to which the sourcing multi-period policy applies
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the product to which the multi-period sourcing policy applies
#### PolicyParameter
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 100.0
	* Used to specify the ratio of the sourcing policy used based on the Site-Product-starting point combination. This parameter takes effect when the policy type is Ratio. The parameter range is 0-100. For example,25 means that when the Site needs to purchase the Product,25% of the purchase volume comes from the source.
#### UnitSourcingCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is 0.0.
	* Indicates the average cost of procuring the unit Product between SourceSite and SiteSite under different Periods, usually including fees such as tariffs, rather than the actual transport cost of the Product. The stepped cost editor can be used to implement the Step costs under different procuring volume.
#### UnitCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Default is empty
	* Reflects the unit carbon emission value within the Period.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Include,options include Include,Exclude
	* Used to specify whether the sourcing policy participates in model optimization:   
	  * Include: sourcing policy participates in model calculation
	  * Exclude: sourcing policy does not participate in model calculation,and will not be used for sourcing. 
#### PolicyPriority
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 1
	* Indicates the modified value of the sourcing policy priority in different periods. This value can be used to modify the policy priority field in the sourcing policy table in a specific period.

_ _ _

## Transportation
### TransportationPolicies
#### SourceName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the source site for transporting the Product.
#### SiteName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the destination that accepts the Product.
#### ProductName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the Product to be transported.
#### ModeName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty
	* Default value is 1
	* Specifies the mode of transportation used between the source and target sites. Different transportation modes could represent different types of transportation (such as FTL, LTL, Parcel) with different costs.
#### ModeFunction
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty
	* Default is LTL, options include LTL and FTL
	* Set the transportation mode for this transportation lane.
#### Distance
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty
	* No default value
	* Defines the distance between the source site and the destination site. If no input is given, a straight-line distance calculated based on longitude and latitude will be used by default.
#### VariableCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty
	* Default value: 0 
	* Set the variable CO2 emissions for this transportation policy based on the 'VariableCO2Basis'
#### VariableCo2Basis
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is Quantity, other options include Volume, Weight, Distance, QuantityDistance, VolumeDistance, WeightDistance
	* Defines the calculation basis for Variable CO2 emission during transportation.
#### PolicyType
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty
	* Default value is First, options include First, SingleMode, and Ratio
	* Indicates the policy of having multiple modes of transportation policy for the same source site-destination site. Not applicable in simulation and will be treated as First.
#### PolicyParameter
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty
	* The default value is 100.0. It takes effect when the policy type is Ratio.
#### ReviewPeriod
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty
	* Default value is 0, and the default unit is day
	* Defines the lenghth of the period that the replenishment demand is reviewed for Cycle stock calculation
#### ReviewSchedule
* **Applicable Algorithms**: SIM

* **Description**:
	* Can be empty
	* No default value
	* Defines the name of a shippment review plan in simulation.
#### ShipmentPeriod
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty
	* No default value
	* Defines the shipment period lenghth for Cycle Stock calculation
#### MaxServiceTime
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty,no default value,default unit is day
	* Indicates the longest service time on the path.
#### MinServiceTime
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty
	* Default value is 0,default unit is day
	* Indicates the shortest service time on the path.
#### DaysBetweenReplenishment
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty
	* Default value is 0
	* Indicates the number of days between receiving the product at the destination.
#### TransportTime
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty
	* Default value is 0
	* Indicates the number of days for goods transportation from the source Site to the destination Site.
#### TransportTimeStd
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty
	* Default value is 0
	* Indicates the standard deviation of the time it takes to transport goods from the source site to the target site.
#### VariableTransportationCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty.
	* Default value is 0.
	* Indicates the unit transportation cost based on variable cost basis,reflected in the total transportation cost in the network summary output table.
#### VariableCostBasis
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty, default value is Quantity, other options include Volume, Weight, Distance, QuantityDistance, VolumeDistance, WeightDistance
	* Defines the calculation basis for Variable Transportation Cost
#### VariableStepCostRule
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty
	* Default value is All
	* Indicates how to apply when variable cost is step cost.
#### FixedShipmentCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty.
	* Default value is 0.
	* Represents the fixed cost for each batch of goods using this particular route and transportation route, reflected in the total transportation cost in the Network Summary output table.
#### ShipmentSize
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty. 
	* Default value is 1. 
	* Represents the average shipment size. For example, if the average shipment size is 50 units, then 100 units of cargo would require 2 trips.                                                                                                                                                                                                                   
#### ShipmentSizeBasis
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty, default value is Quantity, other options include Volume, Weight
	* Defines the calculation basis for Shipment Size
#### ShipmentRule
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty
	* Default value is Ratio
	* Set how shipping batch and fixed shipping costs are applied.
#### MinimalShippingQuantity
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty. 
	* Default value is 0. 
	* Represents the minimum quantity shipped on this route.                                                                                                                                                                                                                                                                                                        
#### Status
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,the default value is Include. It is used to specify whether the transportation policy participates in model optimization.
#### Notes
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the shipping policy,which does not participate in the model calculation.
#### Custom1
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the shipping policy,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the shipping policy,which is convenient for understanding and filtering and does not participate in model calculation.
#### PolicyPriority
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 1
	* When duplicate values appear in this transport policy (same Site,same Product),the transport policy with the smaller number in this field will be used first
#### IncludeInTurns
* **Applicable Algorithms**: NO

* **Description**:
	 * Cannot be empty. Default value is True. Options include True, False. 
	* Set whether this route's volume is included when calculating the "Inventory Estimated by Turnover Rate" output result.                                                                                                                                                                                                     
#### InTransitInvOwnership
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty. Default value is Site. Options include Site, Source. 
	* Set whether in-transit inventory is attributed to the originating site or the destination site.                                                                                                                                                                                                                         
#### EnforceUnitShipment
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, the default value is "False" 
	* Indicates that the volume result of this transportation policy is forced to be an integer.
#### IncludeInDos
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is True,options are True and False
	* Set whether to include the transportation line when calculating DOS output results
#### BundleProducts
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is "False"
	* Set whether to combine the products on this transportation lane when calculating shipment size or step cost. Shipping volume combination is based on same source, destination and transportation mode.

_ _ _

### TransportationPoliciesMultiPeriod
#### PeriodName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Periods defined in the Period table and the groups they consist of (the group type must be Individual)
	* Indicates the Period in which all attributes of the transportation policy take effect.
#### SourceName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is \*Facility,and the group type must be Individual)
	* Indicates the source Site for transporting the Product.
#### SiteName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Sites defined in the Site table and their groups (the group type must be Individual)
	* Indicates the destination that accepts the Product.
#### ProductName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the Product to be transported.
#### ModeName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty, the default value is 1, no specific meaning, you can customize the name of the transportation method
	* Indicates the transportation method between the source site and the target site
	* Transportation mode can be used to model different transportation costs on the same lane.
#### VariableTransportationCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.
	* Indicates the unit transportation cost based on variable cost within this Period, reflected in the total transportation cost in the Network Summary output table.
#### VariableCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Default is empty
	* Reflects the variable carbon emission within the period
#### FixedShipmentCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.
	* Represents the fixed cost for each batch of goods using this transportation policy within a specified Period, reflected in the total transportation cost in the Network Summary output table.
#### PolicyParameter
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,default value is 100.0
	* When policy type is Ratio
	* In simulation,if 30 is filled in,30% of the transportation quantity of source Site-destination Site-Product will be transported in this mode
	* In optimization,if 6 is filled in for one record and 2 is filled in for another,75% will use the mode under the first record,and 25% will use the second mode. You can also fill in a value between 0-1 or 0-100 to represent the ratio. Fill in 0 to exclude this transportation mode.
#### DaysBetweenReplenishment
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,default value is 0
	* Indicates the number of days between the destination receiving the product within the period.
	* Mainly used for calculating demand expansion, safety stock optimization issues. In safety stock optimization, this value is used to calculate the minimum replenishment quantity.
#### ReviewSchedule
* **Applicable Algorithms**: SIM

* **Description**:
	* Can be empty, no default value
	* In optimization, when the replenishment interval days are not filled, the maximum value of the review period and the shipment period is used to calculate the turnover inventory
	* In simulation, it plays the same role as the review period, indicating how often the queue waiting for shipment is inspected. As long as the shipment requirement of this mode is met, the shipment will occur immediately.   
	* Compared with the review period, the shipment review schedule can fill in a finer-grained inspection time or irregular inspection time.   * When the shipment review schedule and the review period are not empty at the same time,only the value of the shipment review schedule is read.
#### Status
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the transportation policy participates in model optimization:
	  * Include: Participate in model calculation   
	  * Exclude: Do not participate in model calculation.
#### PolicyPriority
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 1
	* Indicates the modified value of the transportation policy priority in different periods. This value can be used to modify the policy priority field in the transportation policy table in a specific period.

_ _ _

### FlowConstraints
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value,but for each Period-Start-Site-Product combination,the expression name should be unique
	* This is a custom name for the flow Constraint. Application scenarios include: 
	  1. Create an expression Constraint Group by providing values for Expression 1 and Expression 2,
	  2. Create an expression-based cost by using this value in the "Expression" field,so that you can define the fixed and variable cost components caused by the Constraint
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the drop-down box options are the Periods defined in the Period table and the groups they consist of
	* Indicates the period to which the Constraint applies
	* When the group type is Set,the Constraint will be aggregated over the entire model time,and when the group type is Individual,the Constraint will be applied to each Period.
#### SourceName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the drop-down box options are the Sites defined in the Site table and the groups they form (Site Type is Facility)
	* Indicates the source Site for transporting the Product
	* When the group type is Set,the Constraints will be aggregated on the entire group,and when the group type is Individual,the Constraints will be applied to each group member.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the drop-down box options are the Sites defined in the Site table and the groups they form
	* Indicates the destination that accepts the Product
	* When the group type is Set,the Constraints will be aggregated on the entire group,and when the group type is Individual,the Constraints will be applied to each group member.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the drop-down box options are the products defined in the Product table and the groups they form
	* Indicates the product to be transported
	* When the group type is Set,the Constraints will be aggregated on the entire group,when the group type is Individual,the Constraints will be applied to each group member.
#### ModeName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, the drop-down box options are the transportation modes defined in the transportation policy table and the groups they consist of
	* Indicates the transportation method between the source site and the target site
	* When the group type is Set, the Constraints will be aggregated on the entire group, and when the group type is Individual, the Constraints will be applied to each group member.
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin,Lots,FixedLots,Define
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the quantity of Product required to ship from the source site to the destination site under the Constraint type. For example,refer to [Production Constraint-Constraint value](#Constraint value)
#### CostBasis
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is Quantity,the drop-down box options include: Quantity,Volume,Weight
	* Indicates the unit of the constraint value.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include,optional options include Include,Exclude,
	* Used to specify whether the flow limit participates in model optimization
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about flow limit,not involved in model calculation.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about flow constraints,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about flow constraints,for easy understanding and filtering,and does not participate in model calculation.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 1
	* Indicates the penalty cost for exceeding this limit by 1 unit.
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.

_ _ _

### ShipmentLane
#### SourceName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the drop-down box options are the sites defined in the Site table and their groups (Site Type is \*Facility)
	* Indicates the source site of the transport line.
#### SiteName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the drop-down box options are the Sites defined in the Site table and their groups
	* Indicates the destination that accepts the Product.
#### ProductName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the drop-down box options are the Products defined in the Product table and their groups
	* Indicates the Product to be transported.
#### PeriodName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the drop-down box options are the Period defined in the Period table and its groups.
	* Indicates the period defined for the shipment lane.
#### LaneName
* **Applicable Algorithms**: OA

* **Description**:
	* Define the name of the shipment lane
	* A shipment lane is a combination of transporting a specific Product (group) from a specific origin (or origin group) to a specific Site (group) within a specific Period (group).
#### VariableCost
* **Applicable Algorithms**: OA

* **Description**:
	* Indicates the unit cost on a specific transportation Lane, while the unit basis is defined in the Variable Cost Type in the ShipmentLane table.
	* Step costs can be set.
#### VariableCostBasis
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty, default value is Quantity, other options include Volume, Weight
	* Defines the calculation basis for Variable Cost of each shipment lane
#### VariableCostType
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty, the default value is All, the drop-down box options includ "All" and "Incremental".  
	* All: The cost will be calculated once based on the tier that the total volume falls in, for example (5000,1.5),(10000,1.25), when the output value is 8000, the cost should be 8000\*1.25=10,000
	* Incremental: The unit cost will be calculated based on the each tier discretely, in the above example, when the output value is 8000,the cost should be 5000*1.5+(8000-5000)*1.25=11,250.
#### FixedCost
* **Applicable Algorithms**: OA

* **Description**:
	* Indicates the fixed cost size of a specific shipment lane under a fixed cost baseline.
	* Step costs can be set.
#### FixedCostBasis
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty, default value is Quantity, other options include Volume, Weight
	* Defines the calculation basis for Fixed Cost of each shipment lane
#### ShipmentSize
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty, default value is 1
	* Indicates the size of the shipment batch. If the shipment size is 50, then 100 units of cargo flow requires 2 trips.
#### ShipmentSizeBasis
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the default value is Quantity,options include: Quantity,Weight,Volume,Value,Price
	* Defines the calculation basis for Lot Size of each shipment lane
#### UnitLotCost
* **Applicable Algorithms**: OA

* **Description**:
	* Indicates the transportation cost size for each batch.
#### Status
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the shipment lane participates in model optimization:
	  * Include: Participate in model calculation 
	  * Exclude: Do not participate in model calculation.
#### Notes
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the shipment lane,which is not involved in the model calculation.
#### Custom1
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the transport line,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the transport line,which is convenient for understanding and filtering and does not participate in model calculation.
#### OnTimeRate
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty, default value is 1.00
	* Used to set the minimum on-time delivery order amounts ratio for the transport lane.

_ _ _

### TransitMatrix
#### SourceName
* **Applicable Algorithms**: TO, NO

* **Description**:
	* Cannot be empty,no default value
	* Drop-down box selection,the drop-down box options are Sites defined in the Site table
	* Indicates the Site where the starting point of the trip is located.
#### SiteName
* **Applicable Algorithms**: TO, NO

* **Description**:
	* Cannot be empty,no default value
	* Drop-down box selection,the drop-down box options are Sites defined in the Site table
	* Indicates the Site where the end point of the trip is located.
#### Asset
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty
	* Default value is ALL_TRANSPORTATIONAS_SET. 
	* Dropdown selection. Dropdown options are assets defined in the asset table and groups composed of some assets (group type must be Individual).
	* Indicates the asset used for driving, if you do not need to specify a particular asset for the travel time or distance from the source to the site, just keep the default value.
#### TravelTimeFactor
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value
	* Indicates the adjustment factor of the driving time required for the specified Asset from the starting point to the end point,that is,final driving time = driving time * driving time factor.
#### Distance
* **Applicable Algorithms**: TO, NO

* **Description**:
	* Can be empty,no default value
	* Unit is kilometers
	* Indicates the distance required for the specified asset to travel from the source to the site. If the model detects that this field is empty, the spherical distance will be used instead.
#### IsSymmetric
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty.
	* Default value is Yes. Options include "Yes", "No"
	* Used to clarify whether the distance/time from the site to the source is equal to the distance/time from the source to the site.
#### Status
* **Applicable Algorithms**: TO, NO

* **Description**:
	* Cannot be empty,optional values are Include,Exclude,the default value is Include
	* Indicates whether the specified distance time record participates in model optimization,Include means participation,Exclude means non-participation.
#### AdditiveCost
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value,unit is dollars (or other currency)
	* Generally, additional costs do not need to be filled in. After filling in, the model will add the additional cost to the results of the cost calculation logic from the source to the site (usually referring to tolls, bridge fees,etc.). 
	Note: If both additional costs and override costs are filled in,only the override costs will take effect.
#### OverrideCost
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value.
	* Generally, there is no need to fill in the override cost. After filling it in, the model will use the override cost to override all other cost calculation logic from that source to the site (such as the cost calculated based on the unit distance cost in the Rate table, the cost calculated based on the unit driving time in the Rate table,etc.).
#### TravelTime
* **Applicable Algorithms**: TO, NO

* **Description**:
	* Can be empty,no default value
	* Unit is hours
	* Indicates the time required for the specified Asset to travel from the starting point to the end point. If the model detects that a null value is filled in,it will use the spherical distance divided by the speed of the Asset instead.

_ _ _

### TransportationAsset
#### AssetName
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, no default value
	* Indicates Asset. Commonly used Asset names can be populated here, such as 9.6 meters, 12.5 meters, 18T, ElectricTruck, etc.
#### FixedCost
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,the default value is 0
	* Indicates the fixed cost required for each trip of the Asset,similar to the starting price,including taxi fees.
	Reflected in the total Asset Id fixed cost in the transportation optimization summary output table.
#### IsRoundTrip
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, default value is Yes, options include Yes, No
	* Used to specify whether the asset needs to return to the asset aomicile (the SourceSite in the Asset Assignment table). If it does not need to return to the asset domicile, the asset  will stay where it is after completing all tasks.
#### CapacityQuantity
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty
	* No default value. It is recommended to fill in as a positive integer (filling in a decimal will not cause an error, but it will affect the model calculation and output results), the quantity unit can be customized, but a each model must remain consistent.
	* Indicates the maximum quantity of goods that the Asset is allowed to load. The model will determine whether the Asset can complete the shipment by combining this with the quantity column of "Shipments".
#### CapacityUtilizationRateLimit
* **Applicable Algorithms**: TO

* **Description**:
	* Required, default value is 1.00
	* Indicates the upper limit of the loading rate allowed for the asset. Assume that the maximum load is 5000 (kg), the maximum volume is 60 (cubic meters), the maximum number of loads is empty, and the upper limit of the loading rate is 0.80 in the Asset table. Then the algorithm will load according to the maximum load of 4000 kg and the maximum volume of 48 cubic meters.
#### MaxInTransitStopsPerRoute
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value
	* Indicates the maximum number of sites (excluding asset domicile) that the asset is allowed to stop at in a single trip (starting from the starting point of the asset and returning to the starting point is one trip). If a vehicle operates multiple orders during its stay at a site, or has both unloading and loading operations, it will only be counted as one stop. However, if the asset arrives at a site, leaves the site, goes to another site, and then returns to the site within one trip, the site will be considered as stopped twice. The cost corresponding to the number of stops can be found in the InTransitStopCost field in the Rate table.
#### MaxLoadingStops
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value
	* Indicates the maximum number of sites (excluding asset domicile) allowed for transit and loading operations within a single trip of the asset (from asset domicile departure to returning to domicile). If the asset, within a single trip, arrives at a certain site for loading -> leaves that site to go to another site -> then returns to that site for loading again, that site will be considered as being transited and loaded twice.
#### MaxUnloadingStops
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value
	* Indicates the maximum number of sites where stopovers and unloading operations are allowed within one single trip of the asset (departure from asset source and return to source), excluding the asset domicile. If within one trip, the asset arrives at a site to unload -> leaves that site to go to another site -> then returns to the original site to unload again, that Site is considered a stopover and is counted as two unloading operations.
#### MaxDistancePerRoute
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value, default unit is kilometers
	* Indicates the maximum allowable travel distance within a single trip of the Asset (from Asset Id Source to return to Source)
	* Not currently effective in the Hub optimzation.
#### MaxDistanceBetweenInTransitStops
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value, default unit is kilometers
	* Indicates the maximum distance between two stops for the asset during transportation. Note that the stops do not include the source site of the asset. Therefore,the upper limit of the distance between stops is usually used to prevent the asset from traveling too long between Customers during point-to-point transportation.
#### OverrideMinDistanceBetweenStops
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value,unit is kilometers
	* Assuming the override min distance between stops is filled as 10,the model will treat any distance less than 10 kilometers between two sites as 10 kilometers. This is usually used to prevent the model from underestimating the actual distance between very close sites.
#### MaxDistanceFromAssetSite
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value, default unit is kilometers
	* Assuming that the max distance from asset siteis filled in as 100, then this asset will draw a circle with asset source as the center and a radius of 100 kilometers. For customers outside the circle (i.e., customers whose travel distance from the center exceeds 100 kilometers), this asset will not provide service.
#### VariableServiceTimeBasis
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is Weight ,other options also include Volume and Quantity
	* Defines the calculation basis for the variable service time required of each asset in the loading and unloading operation
#### Speed
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value
	* Indicates the average speed of the asset. When the source site is not recorded in the distance-time matrix input table, the model uses the spherical distance formula to calculate the distance, and then uses this column to calculate the travel time.
#### Organization
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value
	* Indicates the vehicle group that the asset belongs to
	* Not effective yet.
#### Status
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the asset participates in model optimization,Include means participating in model calculation,Exclude means not participating.
#### Notes
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of Customer requirements,which is convenient for understanding and screening and does not participate in model calculation.
#### RestTime
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, default value is 0, default unit is hour
	* Indicates the rest duration required after an asset (driver) has reached the maximum continuous working time, which includes waiting, service (loading and unloading), and driving
	* Not effective in the hub function at current version
#### MaxDutyTimeBeforeRestTime
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty
	* No default value, the default time unit is hours
	* Defines the maximum continuous working time of the Asset. The working time includes waiting, service (loading and unloading) and driving. After the maximum continuous working time,the Asset Id (driver) ought to rest (i.e. stay overnight)
	* Not effective in the Hub function yet.
#### CapacityWeight
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value. It is recommended to fill in a positive integer (filling in a decimal will not cause an error, but it might affect the model calculation and output). The default unit is kilograms, which can be customized to other units, but each model must be consistent.
	* Indicates the maximum weight of the goods that the asset is allowed to load. The model combines the Weight field of the Shipments table to determine whether the asset can complete the transportation task.
#### FixedAssetCost
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,default value is 0
	* Indicates the fixed cost corresponding to using the Asset Id of this Asset,such as rental cost,daily settlement fee,etc. This fixed cost is different from the fixed cost definition in the transportation rate. The fixed cost in the transportation rate refers to the cost of each trip (starting from the starting point of the Asset Id and returning to the starting point is one trip),while the fixed cost in the Asset table is not charged by route. Even if a vehicle runs multiple routes,the fixed cost is only calculated once.
#### CapacityVolume
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value. The default volume unit is cubic meter, accurate to three decimal places (i.e. accurate to cubic decimeter or liter). It can be customized to other unit, but each model must be consistent
	* Indicates the maximum volume of goods that the asset is allowed to load. The model combines the Volume field of the Shipments to determine whether the asset can complete the transportation task.
#### VariableServiceTimeUnload
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,default value is 0
	* Indicates the variable service time required for the unloading operation of the Asset, such as handling and unloading time,in minutes per unit (Weight-kg,Volume-cubic meters,quantity-pieces). Assuming that the fixed service time of an Asset is 10 minutes,the variable unloading time is 0.002 minutes,and the variable loading and unloading basis is Weight, then for an shipment with a Weight of 5000 kg,the total unloading time of the Asset for the shipment is 10+5000*0.002=20 minutes.
#### VariableServiceTimeLoad
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,default value is 0
	* Indicates the variable service time required for the Asset in the loading operation,such as handling and loading time,in minutes per unit (Weight-kg,Volume-cubic meter,quantity-piece). Assuming that the fixed service time of an Asset is 10 minutes,the variable loading time is 2 minutes,and the variable loading and unloading basis is Volume (Volume),then for an shpment with a Volume of 5 cubic meters,the total loading time of the Asset for the order is 10+5*2=20 minutes.
#### FixedServiceTimeUnload
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 0
	* Indicates the fixed service time required for the asset in the unloading operation,such as the vehicle docking, door opening time,etc.,in minutes.
#### VariableServiceTimeBasis
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is Quantity, options include Quantity,Weight,Volume
	* Defines the calculation basis for Variable Service Time of each transportation asset
#### MaxTimePerAsset
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty
	* No default value, the default time unit is hours
	* Defines the maximum total working time of the Asset. Note that working time includes driving, waiting, loading and unloading, but does not include overnight time. Working time starts from the first action of the Asset, whether if it is driving, loading or unloading (not waiting)
#### FixedServiceTimeLoad
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty
	* the default value is 0, default time unit is minutes
	* Defines the fixed service time required for the asset's loading operation, such as docking,hatch opening time,etc.
#### OverrideMinTimeBetweenStops
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty
	* No default value,unit is hour
	* Assuming the shortest driving distance coverage field between sites is set as 0.5,the model will treat the driving time of any two points less than 0.5 hours as 0.5 hours. This is usually used to prevent the model from underestimating the driving time between very close points.
#### MinTimeBetweenRoutes
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,default is 0
	* Indicates the shortest interval time after the asset ends the previous route and returns to the starting point to start the next route.
	* Not effective in the Hub function.
#### MaxTimePerRoute
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value,unit is hours
	* Indicates the maximum total duration of a single route of the Asset (starting from the starting point of the Asset Id and returning to the starting point is one route)
	* Not effective in the Hub function yet.
#### FixedServiceTime
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 0
	* Indicates the fixed service time required for the asset in any loading and unloading operation,such as the time for the asset ID to be parked and docked at the platform,etc.,in minutes. The definition of service includes loading and unloading,and the definition of service time includes fixed and variable parts. Service time can be set through the three dimensions of order,asset,and site (i.e. the corresponding input table). Taking order 1 for unloading from Asset A to Site A as an example,unloading time = fixed service time (SiteA+Asset A+Order 1) + fixed unloading time (SiteA+Asset A+Order 1) + variable unloading time (SiteA+Asset A+Order 1).

_ _ _

### AssetAssignment
#### AssetName
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, no default value
	* Drop-down box selection, the drop-down box options are the Assets defined in the Asset table and the groups composed of some Assets (the group type must be Individual)
	* Indicates the name of the Asset to be assigned.
#### SourceName
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,no default value
	* Drop-down box selection,the drop-down box options are Sites defined in the Site table and groups composed of some Sites (the group type must be Individual)
	* Indicates the starting point location of the Asset,that is,the Asset Domicile.
#### SiteName
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is ALL_SITES,drop-down box selection,the drop-down box options are Sites defined in the Site table and groups composed of some Sites (the group type must be Individual)
	* Except for HubScenario,keep the default value ALL_SITES. In HubScenario,if you fill in "Yes" for trunk long-distance transportation,you need to specify the end point of the trunk in the End Point Name field.
#### AssignedUnits
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value,please fill in a positive integer
	* Indicates the number of assets assigned between the source sites and the destination sites. If you want the model to autonomously decide the number of asset to be used, you can leave the assign unit blank. However, you also need to select “true” in the model options under fleet size optimization.
#### Linehaul
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,input is optional,default value is No,options include Yes,No
	* Used to specify whether the asset is used for linehaul transport,only valid for hub being used. when hub is used, when this field is filled in with Yes,the destination of the linehaul transport needs to be specified in the Destination Site field.
#### RateName
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, no default value, drop-down box selection, the drop-down box options are the rate names defined in the transportation rate table.
	* Indicates the rate name associated with the Asset.
#### Status
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the asset participates in model optimization,Include means participating in model calculation,Exclude means not participating.

_ _ _

### Hub
#### Hub
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, no default value, you need to enter the Site defined in the Site table and its group (the group type must be Individual)
	* Indicates Hub. If the same order allows transportation through multiple Hubs, you need to enter multiple rows in the Hub table to define the relationship between the shipment order and each Hub.
#### ShipmentName
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, drop-down box selection, drop-down box options are shipments defined in the Shipments table
	* Indicates a shipment order. If the same order allows transportation to be completed through multiple hubs, multiple rows need to be entered in the hub table to define the relationship between the shipment order and each hub.
#### ForceThroughHub
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be left blank, input is optional, default value is No. Options include Yes. and No 
	* Indicates whether the shipment must go through the hHub. If Yes is selected, the Shipment will be split into two segments (Source to Hub,Hub to Site) and direct transportation (i.e.,Source to Site) will not be allowed. If No is selected, both segmented transportation and direct transportation are allowed. Note that the same shipment cannot have two or more mandatory hubs..
#### Status
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the Customer order participates in model optimization,Include means participating in model calculation,Exclude means not participating.
#### DirectCostIn
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value, unit is dollars (or other currency)
	* Indicates the direct delivery cost of a shipment from source to hub (i.e.,to the hub segment), such as less-than-truckload (LTL), express delivery,etc. The model will decide from the perspective of optimizing the total cost whether to choose direct delivery for each segment of each Shipment. Generally, please do not set the direct shipping cost to 0.
	* Not effective for now.
#### MaximumDwellTime
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value,units in hours, a positive number greater than the minimum dwell time must be filled in
	* Indicates the maximum allowed dwell time for an shipment in the Hub. The dwell time starts when the shipment entering the Hub is unloaded and ends when the shipment leaving the Hub starts to be loaded.
#### DirectCostOut
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value, unit is dollars (or other currency)
	* Indicates the direct delivery cost of shipment from hub to site (i.e.,from hub segment), such as LTL (less-than-truckload), express delivery,etc. The model will optimize the total cost and decide whether to choose direct delivery for each segment of every shipment. Generally, please do not set the direct shipping cost to 0
	* Not effective for now.
#### MinimumDwellTime
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,default value is 0,unit is hours,must be filled in with a non-negative number
	* Indicates the minimum time the order needs to stay in the hub,such as the registration and scanning time required for cross-docking operations. The dwell time starts from the time the order entering the hub is unloaded and ends when the order leaving the hub starts to be loaded.

_ _ _

### RelationshipConstraints
#### Relationship
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, input is an optional value, default value is Prevent. Options include Force and Prevent
	* Defines the relationship between two types of dimensions,Prevent means to avoid,Force means to enforce.
#### TypeA
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, input is optional, no default value. Dropdown options include Shipments, Sites, Products, and TransportationAsset
	* Define the type of the first element in relationship constraints. For example,if Site1 (due to dock size limitations) is not allowed to be served by Asset 1, you can select Prevent in the relationship field, choose Site in the TypeA field, enter Site1 in IdFieldA, select asset in the TypeB field, and enter Asset 1 in IdFieldB. The types and names of A and B can be interchanged.
	* The allowed TypeA and TypeB for the current model are listed in the table below.
#### IdFieldA
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, no default value, select from the drop-down box, the drop-down box options include Orders/Site/Product/Asset defined in the Order table/Site table/Product table/Asset table and groups consisting of some Orders/Site/Product/Asset (the group type must be Individual)
	* Define the name of the first element in the relationship constraint. For example,if Site1 (due to the size limit of the dock doors) is not allowed to be delivered by Asset A, select Prevent in the relationship, select Site in A-Type, enter Site1 in A-Name, select Asset in B-Type, and enter Asset A in B-Name. The sequence of A and B are interchangeable.
	* The A-types and B-types allowed by the current model are shown in the dropdown.
#### TypeB
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, input is optional, no default value. Dropdown options include Shipments, Sites, Products, and TransportationAsset
	* Define the type of the first element in relationship constraints. For example,if Site1 (due to dock size limitations) is not allowed to be served by Asset 1, you can select Prevent in the relationship field, choose Site in the TypeA field, enter Site1 in IdFieldA, select asset in the TypeB field, and enter Asset 1 in IdFieldB. The types and names of A and B can be interchanged.
	* The allowed TypeA and TypeB for the current model are listed in the table below.
#### IdFieldB
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, no default value, select from the drop-down box, the drop-down box options include Orders/Site/Product/Asset defined in the Order table/Site table/Product table/Asset table and groups consisting of some Orders/Site/Product/Asset (the group type must be Individual)
	* Define the name of the second element in the relationship constraint. For example,if Site1 (due to the size limit of the dock doors) is not allowed to be delivered by Asset A, select Prevent in the relationship, select Site in A-Type, enter Site1 in A-Name, select Asset in B-Type, and enter Asset A in B-Name. The sequence of A and B are interchangeable.
	* The A-types and B-types allowed by the current model are shown in the dropdown.
#### Status
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the Customer order participates in model optimization,Include means participating in model calculation,Exclude means not participating.
#### Notes
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of Customer requirements,which is convenient for understanding and screening and does not participate in model calculation.

_ _ _

### PeriodicSchedule
#### SiteName
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,no default value
	* The options in the drop-down menu include ALL_SITES,ALL_SITES_SET,user-defined Site groups,and non-Customer type data in the Site table
	* When selecting a group such as ALL_SITES,if the group contains Customer type Sites,such Customer Sites will not take effect,and only the costs of Facility type Sites will be generated.

_ _ _

### ShipmentConstraints
#### Status
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,optional values are Include,Exclude,the default value is Include
	* Indicates whether the specified shipment Constraint record participates in model optimization,Include means participation,Exclude means non-participation.
#### DeliverySequence
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value
	* Indicates the unloading sequence of the shipment in this route. Please use integers,from small to large to represent from first to last. Integers can be discontinuous (for example,fill in 1,3,5,6 in different rows of the same route,but no repeated numbers). Note: You can fill in only one of the two columns for the loading sequence number and unloading sequence number.
#### PickupSequence
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value
	* Indicates the loading sequence of the shipment in this route. Please use integers,from small to large to represent from first to last. Integers can be discontinuous (for example,fill in 1,3,5,6 in different rows of the same route,but no repeated numbers). Note: You can fill in only one of the two columns of loading sequence number and unloading sequence number.
#### BaselineSolution
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value
	* Indicates the name of the Baseline Solution, such as "Baseline" or "Optimized", which is convenient for building scenario items to filter Shipment Constraint records that need to be considered by the model.
#### ShipmentName
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, no default value
	* Dropdown selection, dropdown options are defined by the Shipments table
	* Indicates the shipments the constraints apply to.
#### AssetName
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value
	* Dropdown selection, dropdown options are defined by the Transportation Asset table
	* Indicates the Asset restricted for use by this Shipment. Note that when filling out, the Asset for different rows on the same Route should be the same. If not filled out, it indicates no Constraint on Asset usage.
#### AssetDomicile
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value
	* Dropdown selection, dropdown options as defined in Site table
	* Indicates the Asset Domicile Site of the Asset that this Shipment is restricted to. Please ensure that the Asset Domicile Name for different rows of the same Route is consistent. If left blank, it means there is no Constraint on using the Asset's Domicile.
#### Route
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty, no default value
	* Indicates the name of the route to which a transport order belongs. Multiple records with the same name belong to the same route. It is recommended to use an ID code (for example, "Asset name-Asset Id serial number-Route serial number", "3m5-1-2").

_ _ _

## Inventory
### InventoryPolicies
#### SiteName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value
	* No need for uniqueness The drop-down box options are Sites (Site Type = ExistingFacility or PotentialFacility) defined in the Site table and groups composed of Sites (the group type must be Individual),indicating the destination for storing the Product.
#### ProductName
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,no default value
	* No need for unique drop-down box options for the Product table defined Products and their groups (group type must be Individual)
	* Indicates the Product to be stored.
#### PolicyType
* **Applicable Algorithms**: SIM

* **Description**:
	* Can be empty,default value is s_S,dropdown options include: 
	* s_S: This is a minimum/maximum inventory policy. When the inventory level is below s, the site will generate a replenishment shipment to restock the inventory up to S. 
	* R_Q: This is a fixed reorder point/fixed reorder quantity policy. When the inventory level is below a certain reorder point R, the site will generate a replenishment shipment for the product with the quantity Q, until the inventory level exceeds R. 
	* T_S: This is a periodic review policy to replenish inventory to a certain level, and is preferred in situation with intermittent demand as it helps consolidate supplier shipments.
	* Indicates the type of relationship between reorder points and replenishment quantities.
#### StockingSite
* **Applicable Algorithms**: NO, SSO

* **Description**:
	* Cannot be empty,the default value is True,no need for unique drop-down box options including True,False,if False is filled in,it means that this site cannot store this product and the inventory is 0.
#### Parameter1
* **Applicable Algorithms**: SIM

* **Description**:
	* Cannot be empty,default value is 0
	* When the policy type is R*Q or s*S,it indicates the reorder point that triggers the replenishment order.
#### Parameter2
* **Applicable Algorithms**: SIM

* **Description**:
	* Cannot be empty,default value is 0
	* Depending on the policy type,it indicates the order quantity or the quantity to be ordered to a certain inventory level. When the policy type is R*Q,it indicates a fixed order quantity. When the policy type is s*S,it indicates the quantity of the target inventory level that must be replenished.
#### InitialInv
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty, default value is 0,no need to be unique
	* Indicates the initial stock of the Site, safety stock optimization does not consider initial stock.
	Deprecated,should preferably use the initial inv table.
#### SafetyStock
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 0,no need to be unique
	* Indicates the minimum amount of safety stock that SiteProduct should keep at the end of each Period. This value can be calculated based on safety stock optimization. Deprecated,it is recommended to use the Inventory Constraint table to set the target of the end-of-period inventory
#### ReviewPeriod
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Cannot be empty,default value is 0,default unit is day,no need to be unique
	* Indicates how often the product is checked in the current warehouse,and when the replenishment basis is reached,a replenishment order is generated.
#### ReviewSchedule
* **Applicable Algorithms**: SIM

* **Description**:
	* Can be empty,no default value,default unit is day
	* Indicates how often the inventory level is checked. As long as the inventory standard of this mode is reached,inventory occurs immediately.
#### ServiceType
* **Applicable Algorithms**: SSO

* **Description**:
	* Can be empty,default value is Type_1, no need to be unique
	* Indicates the requirement for the site's service level, indicating how to evaluate the inventory rate.
#### MaxServiceTime
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty,default value is 0,default unit is day,no need to be unique
	* Indicates the hard constraint of the maximum service time of the site for the downstream site.
#### MinServiceTime
* **Applicable Algorithms**: SIM, SSO

* **Description**:
	* Can be empty,default value is 0,default unit is day,no need to be unique
	* Indicates the hard constraint of the shortest service time of the site for the downstream site.
#### RelaxCustomerServiceTime
* **Applicable Algorithms**: SSO

* **Description**:
	* Cannot be empty,default value is False,no need to be unique
	* Automatically set the range for the latest delivery time allowed for SiteProduct
#### EnforceRiskPooling
* **Applicable Algorithms**: SSO

* **Description**:
	* Cannot be empty,default value is False,no need to be unique.
	Set the forced risk coverage days for SiteProduct to 0/MaxLeadTime/ImmediateLeadTime
#### ServiceLevel
* **Applicable Algorithms**: SSO

* **Description**:
	* Cannot be empty,default value is 0.95,no need to be unique
	* Represents the fulfillment rate of the Product supplied to the Customer-facing Site based on the service level type.
#### UnitCo2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 0,and it does not need to be unique. It reflects the carbon emission value of the storage unit material within the Period.
#### MinDwellTime
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0, no need to be unique
	* Indicates minimum number of days a product stays in the warehouse
#### MaxDwellTime
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0, no need to be unique
	* Indicates maximum number of days a product stays in the warehouse
#### VariableInboundCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is 0.  
	* Indicates the variable cost of inbounding each Product unit.
#### VariableOutboundCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.
	* Indicates the variable cost of outbounding for each Product unit.
#### HandlingCostBasis
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Quantity, other options include Volume and Weight
	* Defines the calculation basis for Variable Inbound Cost and Variable Outbound Cost of site-product inventory policy
#### VariableStorageCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is 0.
	* Represents the variable storage cost per unit of Product in the model horizon.
#### StorageCostBasis
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Quantity, other options include Volume and Weight
	* Defines the calculation basis for Variable Storage Cost of site-product inventory policy
#### ProductInvValue
* **Applicable Algorithms**: NO, SSO

* **Description**:
	* Can be empty, no default value
	* Represents the currency value per unit of the product, used to calculate inventory holding costs. In network optimization and inventory optimization, the product value of the inventory policy table will overwrite the product value in the product table, while the simulation always uses the product value in the product table.
#### InvCarryingCostPct
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, no default value.
	* Indicates the inventory holding cost of the Product stored at this Site during the model horizon. If this field is not filled in, the  model will take the default value of the inventory holding cost set in the Model Options.
#### InvTurns
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* No need to be unique
	* Indicates the number of inventory turnovers within the Period time,used to calculate the Period inventory level and inventory holding cost based on turnover
#### FixedStockingTime
* **Applicable Algorithms**: SIM

* **Description**:
	* When a warehousing event is triggered,if a fixed warehousing time is used,the warehousing time does not change with the product quantity.   
	* The unit is day.
#### UnitStockingTime
* **Applicable Algorithms**: SIM

* **Description**:
	* When an event triggers the warehousing, if the unit warehousing time is used, the total warehousing time varies with the quantity of products.
	* The warehousing time is the unit warehousing time multiplied by the quantity of products, measured in days.
	* If both fixed warehousing time and unit warehousing time are configured simultaneously, the output result is the sum of the two.
#### FixedPickingTime
* **Applicable Algorithms**: SIM

* **Description**:
	* When an event triggers the outbound process, if fixed outbound time is used, the outbound time does not vary with the quantity of products.
	* Unit is in days.
#### UnitPickingTime
* **Applicable Algorithms**: SIM

* **Description**:
	* When the event of outbound delivery is triggered,if the unit outbound delivery time is used,the total outbound delivery time varies with the number of products.   
	* The outbound delivery time is the unit outbound delivery time multiplied by the number of products.  
	* The unit is day.
#### DisposalCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.
	* At each site, this field indicates the disposal cost of the product/sub-product/waste with shelf life.
#### Status
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Cannot be empty,the default value is Include,no need to be uniquely used to specify whether the inventory policy participates in model optimization
#### Notes
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about the inventory policy,which is not involved in the model calculation.
#### Custom1
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the inventory policy,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO, SIM, SSO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the inventory policy,which is convenient for understanding and filtering and does not participate in model calculation.
#### TransformationId
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default is DEFAULT,no need to be unique
	Related to the model transformation function. Through the “Output Table - Safety Stock Strategy Summary” “Add to Inventory Strategy Table” button,the results can be imported into the “Input Table - Inventory Strategy” to achieve the conversion of SSO output results to NO,SIM input. This Column records the source Scenario of the inventory policy.
#### PolicyPriority
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 1
	* When duplicate values appear in this inventory policy (same Site,same Product),the inventory policy with the smaller number in this field will be used first

_ _ _

### InventoryPoliciesMultiPeriod
#### PeriodName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty. The drop-down box options are the Periods defined in the Period table and the groups they consist of (the group type must be Individual).
	* Indicates the Period in which all attributes of the inventory policy take effect.
#### SiteName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Sites defined in the Site table and their groups (the group type must be Individual)
	* Indicates the destination for storing the Product.
#### ProductName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the drop-down box options are the Products defined in the Product table and their groups (the group type must be Individual)
	* Indicates the Product to be stored.
#### Parameter1
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,default value is 0
	* When the policy type is R*Q or s*S,it indicates the reorder point that triggers the replenishment order.
#### Parameter2
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,default value is 0
	* Depending on the policy type,it indicates the order quantity or the quantity to be ordered to a certain inventory level. When the policy type is R*Q,it indicates a fixed order quantity. When the policy type is s*S,it indicates the quantity of the target inventory level that must be replenished.
#### SafetyStock
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,default value is 0
	* Indicates the safety stock of SiteProduct in this Period,this value can be calculated based on safety stock optimization.
#### UnitCo2
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Default is empty
	* Reflects the unit carbon emission value within the Period.
#### VariableInboundCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0
	* Indicates the variable cost of inbounding each Product unit within a certain Period.
#### VariableOutboundCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0
	* Indicates the variable cost of outbounding each Product unit within a certain Period.
#### VariableStorageCost
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, default value is 0.
	* Indicates the variable storage cost of each Product unit in a certain Period.
#### InvCarryingCostPct
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,no default value
	* Indicates the inventory holding cost of the Product stored at this Site during the Period as a percentage of the Product value
	* Reflected in the total inventory holding cost in the network summary table.
#### ProductInvValue
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, no default value.
	* Indicates the value of each unit of Product in a certain Period, which is used to calculate inventory holding cost:   
	* Inventory holding cost = inventory quantity \* Product value \* holding cost rate \* period length
	* In network optimization and inventory optimization, the Product value defines in the inventory policy will overwrite the Product value defined in the Product table, while during simulation computing, the model will always read the Product Value from the Product table.
#### Status
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the inventory policy in this Period participates in model optimization:   
	  * Include: Participate in model calculation   
	  * Exclude: Do not participate in model calculation
#### ReviewSchedule
* **Applicable Algorithms**: SIM

* **Description**:
	* Can be empty,no default value
	* Set up stock check schedule in simulation algorithm
	* Setting method 1: According to calendar schedule
	* Setting method 2: According to weekly schedule
	* Setting method 3: According to fixed period schedule
#### PolicyPriority
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 1
	* Indicates the modified value of the inventory policy priority in different periods. This value can be used to modify the policy priority field in the inventory policy table in a specific period.
#### InvTurns
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,no default value
	* Specify a parameter,which can be used to calculate the average inventory
	* Average Inventory = m * Throughput,where m is the reciprocal of the inventory turnover rate

_ _ _

### InitialInventory
#### SiteName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,no default value
	* The drop-down box options are the Sites defined in the Site table and the groups they form (the group type must be Individual)
	* Indicates the location where the Product is stored at the beginning of the period.
#### ProductName
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,no default value
	* No need for unique drop-down box options for the Product table defined Products and their groups (the group type must be Individual),indicating the Products stored at the beginning of the period.
#### ProductionDate
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, no default value.   
	* Indicates the production date of the Product.
#### AvailableDate
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,no default value.   
	* Indicates the date when the Product can be used.
#### InventoryType
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty, inputs are selectable values. Default value is On Hand. Options include On Hand, In Transit, and Work In Process
	* Indicates the form of the initial inventory: 
	  * On Hand: On Hand Inventory
	  * In Transit: In Transit Inventory
	  * Work In Process: Work In Process Inventory
#### Quantity
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,no default value
	* Does not need to be unique. Can be an integer or a decimal. The unit can be customized,but must be consistent. Indicates the number of Products held or in transit at the site at the beginning of the period.
#### Status
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Cannot be empty,the default value is Include,no need to be uniquely used to specify whether the beginning inventory participates in model optimization
#### Notes
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the beginning inventory,which is not involved in the model calculation.
#### Custom1
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the beginning inventory,which is convenient for understanding and filtering and does not participate in model calculations.
#### Custom2
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty.
	* No default value.
	* Indicates any other custom information related to initial inventory, making it easier to understand and filter, which is not involved in the model calculation.
#### Custom2
* **Applicable Algorithms**: NO, SIM

* **Description**:
	* Can be empty,no default value
	* Not required to uniquely represent an optional descriptive statement about the beginning inventory,not involved in model calculations.

_ _ _

## Advanced Constraint
### ExpressionConstraintGroup
#### ConstraintGroupName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,can be repeated,a group will be created when the same name is used.   
	* Indicates the name of the group created by the expression Constraint
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are expressions defined in each constraint table
	* Indicates the group members in the expression Constraint Group
#### Coefficient
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is 1.0
	* Indicates the coefficient of the calculation relationship of each expression in the expression constraint group.   
	* For example,if the expression constraint group definition is: 1*"expression 1"-3*"expression 2",the coefficient of expression 1 is 1,and the coefficient of expression 2 is -3.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the expression Constraint Group participates in model optimization:   
	  * Include: The expression Constraint Group participates in model calculation
	  * Exclude: The expression Constraint Group does not participate in model calculation and will not be used in expression Constraints.

_ _ _

### ExpressionConstraints
#### ConstraintGroupName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,can be repeated,a group will be created when the same name is used.
	* Indicates the expression to which the expression constraint applies.
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin,Lots,FixedLots,Define
	* Used to specify the type of expression group Constraint:   
	* Min: The total amount of the expression group must be greater than or equal to the Constraint value
	* Max: The total amount of the expression group must be less than or equal to the Constraint value
	* Fixed: The total amount of the expression group must be equal to the Constraint value
	* CondMin: The total amount of the expression group can be 0,if not 0,it must be greater than or equal to the Constraint value
	* Lots: Define the batch size (the actual quantity may not be an integer multiple of the batch),the final calculated Lots quantity will be rounded up
	* FixedLots: Define the batch size (the actual quantity must be an integer multiple of the batch),if the actual quantity is not an integer multiple,the model will be infeasible
	* Define: Used to create an expression,no Constraint value is required
	* When Lots and FixedLots limit the batch quantity,it indicates the combined batch of different expressions in the Constraint Group
	* When Define is selected,the Constraint Group is generally used to call the "Expression Cost" table,and it is not recommended to use it again for "Expression Constraint Group" table to create a group.
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the limit amount specified by this Constraint
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the expression Constraint Group participates in model optimization:   
	  * Include: The expression constraint participates in model calculation
	  * Exclude: The expression constraint does not participate in model calculation and will not be used for Constraint.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 1
	* Indicates the unit penalty cost for breaking the limit of this expression,effective when the "IsSoftConstraint" field is "True"
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.

_ _ _

### FlowCountConstraints
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value,
	* This is an optional name for a flow count Constraint,which can be used to: 
	  1. Create an expression Constraint Group by providing values for Expression1 and Expression2,
	  2. Create an expression-based cost by using this value in the Expression field,enabling the definition of fixed and variable cost components resulting from the Constraint
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table,or the Period group,indicates the Period to which the flow count limit applies,can be a single Period,it can be an Individual Period group,representing the count limit that exists in each Period,or it can be a SET Period group,representing the count limit summarized by this Period group
#### SourceName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and the groups they form (Site Type is Facility),indicates the starting site for the flow count limit,
	* If the Individual group is selected,it means that each individual member in the group has an independent limit,and if the SET group is selected,it means the count limit for the collected group of all the members.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and the groups they form,
	* Indicates the end site to which the flow count limit applies,
	* If the Individual group is selected,it means that each individual member in the group has an independent limit,and if the SET group is selected,it means the count limit for the group members in total
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the products defined in the Product table and the groups they form,
	* Indicates the product to which the flow count limit applies,
	* If the Individual group is selected,it means that each member in the group has its own independent limit,and if the SET group is selected,it means the count limit for the group members in total
#### ModeName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, no default value, the drop-down box options are the transportation modes and groups defined in the transportation policy table,
	* Indicates the transportation mode to which the flow count limit applies,
	* If an Individual group is selected, it means that each individual member in the group has independent Constraints, and if a SET group is selected, it means the cumulative count of group members.
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin,Define
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value,indicates the amount of limit,here refers to the number of counts
#### PeriodAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, input as optional value, default value is True, options include True,False
	* Used to specify whether to aggregate Period:   
	  * True: Aggregate Period, not a field for counting
	  * False: Do not aggregate Period, it is a field for counting.
#### SourceAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, input is optional, default value is True, options include True, False
	* Used to specify whether to aggregate the starting point:   
	  * True: Aggregate the starting point, not the field used for counting
	  * False: Do not aggregate the starting point, it is a field used for counting.
#### SiteAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,input as optional value,default value is True, options include True, False
	* Used to specify whether to aggregate Site:   
	  * True: Aggregate Site, not a field for counting
	  * False: Do not aggregate Site, it is a field for counting.
#### ProductAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, input as optional value, default value is True, options include True, False
	* Used to specify whether to aggregate Product:   
	  * True: Aggregate Product, not a field for counting
	  * False: Do not aggregate Product, it is a field for counting.
#### ModeAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, input is optional, default value is True, options include True, False
	* Used to specify whether to aggregate transportation modes:      
	  * True: Aggregate transportation modes, not a field for counting
	  * False: Do not aggregate transportation modes, it is a field for counting.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude,
	* Used to specify whether the flow count limit participates in model optimization
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive statement about the flow count limit,which does not participate in the model calculation.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the flow count limit,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the flow count limit,which is convenient for understanding and filtering and does not participate in model calculation.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 1,represents the unit penalty cost for violating the flow count constraint
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.

_ _ _

### GreenFieldServiceConstraints
#### Expression
* **Applicable Algorithms**: GF

* **Description**:
	* Can be empty,no default value
	* Expression name must be unique This is an optional name for a location service constraint.
#### SiteName
* **Applicable Algorithms**: GF

* **Description**:
	* Cannot be empty,no default value. The drop-down box options are the non-facility Customers and their groups defined in the Site table,indicating the Customers to which the site selection service Constraints apply.
#### Distance
* **Applicable Algorithms**: GF

* **Description**:
	* Cannot be empty
	* Default value is 100
	* Indicates the distance that needs to be met for the location service Constraint.
#### Percentage
* **Applicable Algorithms**: GF

* **Description**:
	* Cannot be empty,default value is 100
	* Indicates the percentage of location service constraints that need to be met.
#### Status
* **Applicable Algorithms**: GF

* **Description**:
	* Cannot be empty,the default value is Include. It is used to specify whether the location service Constraint participates in model optimization.
#### Notes
* **Applicable Algorithms**: GF

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the location service Constraints,which does not participate in the model calculation.

_ _ _

### CustomerServiceConstraints
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* This is the optional name of the Customer service constraint
	* Not available for Expression Cost,Expression Constraint Group,Expression Constraint.
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table
	* Indicates the Period to which the Customer service Constraint applies.
#### SourceName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is Facility,and the group type must be Individual)
	* Indicates the source Site for transporting the Product.
#### CustomerName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the drop-down box options are Customer (Site Type=Customer) defined in the Site table and groups composed of Customers
	* Indicates the Customer or Customer group to which the Customer service Constraint applies.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the drop-down box options are the Products defined in the Product table and the groups they form
	* Indicates the Product or Product group to which the Customer service Constraint applies.
#### ModeName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, no default value, the drop-down options are the transportation modes and their groups defined in the transportation policy table
	* Indicates the mode applicable to customer service constraints
#### Distance
* **Applicable Algorithms**: NO

* **Description**:
	* The maximum transportation distance of the Customer service. The shipment quantity exceeding the maximum distance will not be counted as the shipment quantity that meets the service requirements.
#### Duration
* **Applicable Algorithms**: NO

* **Description**:
	* The maximum transportation time for customer service; shipments exceeding the maximum transportation time do not count as shipments that meet the service requirements.
#### CostBasis
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Quantity,options include Quantity,Volume,Weight
	* basis used to specify Customer service constraint value:   
	  * Quantity: Quantity  
	  * Volume: Volume  
	  * Weight: Weight  
	* The units of each field in the model must be consistent (no default unit)
#### Percentage
* **Applicable Algorithms**: NO

* **Description**:
	* Customer service percentage limit,which limits the number of shipments within the maximum service time/distance to the minimum percentage of the total shipments.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the location service Constraint participates in the model optimization:   
	  * Include: Customer service Constraints participate in model calculation
	  * Exclude: Customer service Constraints do not participate in model calculation and will not be used for Constraints.
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the location service Constraints,which does not participate in the model calculation.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,the default value is 1,represents the unit penalty cost for violating the Customer service constraint value constraint
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.

_ _ _

### InventoryConstraints
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* This is an optional name for an inventory Constraint. Expressions created by inventory Constraints can be used in:  
	  * Create an expression Constraint by specifying an expression for the value of either expression1 or expression2. Enables combining Constraints
	  * Creates expression-based costs by using defined expression names in the Expression Cost table,enabling definition of fixed and variable costs resulting from Constraints.
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table
	* Indicates the Period to which the Inventory Constraint applies.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is Facility)
	* Indicates the Site to which the Inventory Constraint applies.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Products defined in the Product table and their groups
	* Indicates the Products to which the Inventory Constraint applies.
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin,Define
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the limit amount specified by this Constraint
#### CostBasis
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is Quantity,options include Quantity,Volume,Weight
#### PreBuildStock
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,input is optional,default value is True,options include True,False
	* Used to specify whether the constraint is applied to pre-placed inventory:   
	  * True: The constraint will be applied to pre-placed inventory
	  * False: The constraint will not be applied to pre-placed inventory.   
	* If all inventory types are selected to be excluded (ie False),then the constraint will be ignored.
#### SafetyStock
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,input is optional,default value is False,options include True,False
	* Used to specify whether the constraint is applied to safety stock:   
	  * True: The constraint will be applied to safety stock
	  * False: The constraint will not be applied to safety stock.
#### CycleStock
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,input is optional,default value is False,options include True,False
	* Used to specify whether the constraint is applied to cycle stock:   
	  * True: The constraint will be applied to cycle stock
	  * False: The constraint will not be applied to cycle stock.
#### TurnEstimatedStock
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,input is optional,default value is False,options include True,False
	* Used to specify whether the constraint is applied to the turn estimate stock: 
	  * True: The constraint will be applied to the turn estimate stock
	  * False: The constraint will not be applied to the turn estimate stock.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Include,optional options include Include,Exclude
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive statement about Inventory Constraints,not involved in model calculations.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about Inventory Constraints,for easy understanding and filtering,not involved in model calculations.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about Inventory Constraints,for easy understanding and filtering,not involved in model calculations.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 1.0
	* Indicates the unit penalty cost of the inventory exceeding the Inventory Constraint. The unit corresponds to the setting in "Inventory Constraint - Constraint Value Basis" (special case: if "Constraint Value Basis" is "DOS",the unit penalty cost calculation unit is Quantity).
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.

_ _ _

### InventoryCountConstraints
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* This is an optional name for a stock count Constraint. Expressions created by stock count Constraints can be used in:                                                                   
	  * Create an expression Constraint by specifying anexpression for the value of either expression1 or expression2. Enables combination of Constraints
	  * Creates expression-based costs by using defined expression names in the Expression Cost table,enabling definition of fixed and variable costs resulting from Constraints.
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table
	* Indicates the Period to which the inventory count constraint applies.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is Facility)
	* Indicates the Site to which the inventory count constraint applies.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Products defined in the Product table and their groups
	* Indicates the Product to which the inventory count constraint applies.
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin,Define
	* Type used to specify inventory count constraint:   * Min: The inventory count quantity must be greater than or equal to the constraint value
	* Max: The inventory count quantity must be less than or equal to the constraint value
	* Fixed: The inventory count quantity must be equal to the constraint value
	* CondMin: The inventory count quantity can be 0,if not 0,it must be greater than or equal to the constraint value
	* Define: Used to create an expression,no constraint value is required.
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the limit amount specified by this Constraint
#### PeriodAggregated
* **Applicable Algorithms**: NO

* **Description**:
	*  Can be empty, input is optional. Default value is True, options include True and False
	* Used to specify whether to aggregate period: 
	  * True: aggregates period, not used for the counting Column
	  * False: does not aggregate period, used for the counting Column.
#### SiteAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, input as optional value. Default value is True, options include True and False
	* Used to specify whether to aggregate sites:
	  * True: aggregate sites, not a column used for counting.
	  * False: do not aggregate sites, it is a column used for counting.
#### ProductAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, input optional. Default value is True, options include True and False
	* Used to specify whether to aggregate products:
	  * True: aggregate products ,not a column for counting
	  * False: do not aggregate products, is a column for counting.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the inventory count constraint participates in model optimization:   
	  * Include: The inventory count constraint participates in model calculation
	  * Exclude: The inventory count constraint does not participate in model calculation and will not be used for Constraint.
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive statement about the inventory count constraint,which does not participate in the model calculation.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about inventory count constraints,for easy understanding and filtering,not involved in model calculations.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about inventory count constraints,for easy understanding and filtering,not involved in model calculations.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 1
	* Indicates the unit penalty cost for exceeding the inventory count constraint,effective when the "IsSoftConstraint" field is "True"
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.

_ _ _

### ProductionCountConstraints
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* This is an optional name for a production count constraint. Expressions created by production count constraints can be used in the following ways:
	* Create expression constraints by specifying an expression for the value of expression1 or expression2. Enables the combination of constraints
	* Creates expression-based costs by using the defined expression name in the Expression Cost table,enabling the definition of fixed and variable costs resulting from the constraint.
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Periods defined in the Period table
	* Indicates the Period to which the production count constraint applies.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is \*Facility)
	* Indicates the Site to which the production count constraint applies.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Products defined in the Product table and their groups
	* Indicates the Products to which the production count constraint applies.
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin,Define
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the limit amount specified by this Constraint
#### SiteAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, input is optional. Default value is True, options include True and False
	* Used to specify whether to aggregate sites:
	  * True: aggregate sites, not used for counting column
	  * False: do not aggregate sites, used for counting column.
#### ProductAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, input optional. Default value is True, options include True and False
	* Used to specify whether to aggregate products:
	  * True: aggregate products ,not a column for counting
	  * False: do not aggregate products, is a column for counting.
#### PeriodAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,input is optional,default value is True,options include True,False
	* Used to specify whether to aggregate Period: 
	  * True: Aggregate Period,not a field for counting
	  * False: Do not aggregate Period,it is a field for counting.
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive statement about the production count constraint,which does not participate in the model calculation.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Include,optional options include Include,Exclude
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the production count constraint,for easy understanding and filtering,and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the production count constraint,for easy understanding and filtering,and does not participate in model calculation.
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 1.0
	* Indicates the unit penalty cost for the production count exceeding the production count constraint.

_ _ _

### SiteConstraints
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Expression name must be unique. This is an optional name for a Site Count Constraint. Expressions created by Site Count Constraints can be used in the following ways: Creating expression constraints by specifying an expression for the value of expression1 or expression2,allowing constraints to be combined,Creating expression-based costs by using a defined expression name in the Expression Cost table,allowing the definition of fixed and variable costs resulting from constraints.
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table
	* Indicates the Period to which the Site count limit applies.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the site to which the site count limit applies.
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value. Used to specify the type of Site Constraint.
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the limit amount specified by this Constraint
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include. Used to specify whether the Site count limit participates in model optimization.
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive description of the Site count limit,which does not participate in model calculations.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the Site count limit,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the Site count limit,which is convenient for understanding and filtering and does not participate in model calculation.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty
	* The default value is 1. It is used to set the penalty cost per unit when the soft constraint is not met.
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.

_ _ _

### WorkCenterConstraints
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* This is an optional name for a Site Count Constraint. Expressions created by Site Count Constraints can be used in the following ways:
	* Create an expression constraint by specifying an expression for the value of either Expression1 or Expression2. Enables the combination of constraints
	* Creates expression-based costs by using a defined expression name in the Expression Cost table,enabling the definition of fixed and variable costs resulting from constraints.
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table
	* Indicates the Period to which the Site count limit applies.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is Facility)
	* Indicates the Site to which the Site count limit applies.
#### WorkCenter
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Options in the dropdown list are the work centers defined by the Work Center table and their composed groups
	* Defines the applicable work centers for the Work Center Constraints,
	  * If 'Individual' group is selected, the constraint will be applied respectively on each member of the individual group. 
	  * If 'Set' group is selected, the constraint will be applied collectively on the set group as a whole.
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin,Define
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the limit amount specified by this Constraint
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Include,optional options include Include,Exclude
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive description of the Site count limit,which does not participate in model calculations.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the Site count limit,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about Site count limits,for easy understanding and filtering,and does not participate in model calculation.
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 1.0
	* Indicates the unit penalty cost when the number of work center openings exceeds the work center constraint.

_ _ _

### ShipmentLaneConstraints
#### SourceName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the drop-down box options are the sites defined in the Site table and their groups (Site Type is Facility,and the group type must be Individual)
	* Indicates the starting point of the shipment lane.
#### SiteName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the drop-down box options are Customer (Site Type=Customer) defined in the Site table and a group consisting of some Customers
	* Indicates the end point of the transportation route.
#### ProductName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the drop-down box options are the products defined in the Product table and the groups they form
	* Indicates the product or product group to which the transportation route Constraint applies.
#### PeriodName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table
	* Indicates the Period to which the transportation route Constraint applies.
#### LaneName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty, no default value, the drop-down box options are the shipment lanes defined in the shipment lane table.
	* Indicates the shipment lanes to which the shipment lane Constraints apply.
#### ConstraintType
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin
	* Used to specify the type of shipment lane Constraints:   
	  * Min: route flow must be greater than or equal to the Constraint value
	  * Max: route flow must be less than or equal to the Constraint value
	  * Fixed: route flow must be equal to the Constraint value
	  * CondMin: route flow can be 0,if not 0,it must be greater than or equal to the Constraint value.
#### ConstraintValue
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Indicates the size of the lane flow under the Constraint type.
#### CostBasis
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,the default value is Quantity,the drop-down box options include: Quantity,Volume,Weight,Value,Price
	* Indicates the unit of the constraint value,Value is the value,and Price is the price.
#### IsSoftConstraint
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: OA

* **Description**:
	* Used to set the penalty cost when the soft constraint is not met.
	* For example,if the Constraint type is Max,the Constraint value is 100,the Constraint value base is Value,IsSoftConstraint is True,and the soft constraint penalty cost is 10,it means that when the lane flow value exceeds 100 dollars,a penalty cost of 10 dollars is required for every 1 dollars exceeding the value.
#### Status
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the transportation route Constraints are involved in model optimization:   
	  * Include: Transportation route Constraints are involved in model calculation
	  * Exclude: Transportation route Constraints are not involved in model calculation,and the model will not consider transportation route Constraints.
#### Notes
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the shipment lane Constraints,which does not participate in the model calculation.
#### Custom1
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about transportation line Constraints,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about transportation line Constraints,which is convenient for understanding and filtering and does not participate in model calculation.

_ _ _

### ShipmentLaneCountConstraints
#### SourceName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the drop-down box options are the sites defined in the Site table and their groups (Site Type is Facility,and the group type must be Individual)
	* Indicates the starting point of the shipment lane.
#### SiteName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the drop-down box options are Customer (Site Type=Customer) defined in the Site table and a group consisting of some Customers
	* Indicates the end point of the transportation route.
#### ProductName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the drop-down box options are the products defined in the Product table and the groups they form
	* Indicates the product or product group to which the transportation route Constraint applies.
#### PeriodName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Period defined in the Period table
	* Indicates the Period to which the transportation route Constraint applies.
#### LaneName
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty, no default value, the drop-down box options are the shipment lanes defined in the shipment lane table.
	* Indicates the shipment lanes to which the shipment lane Constraints apply.
#### SourceAggregated
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty, input is optional, default value is True, options include True,False
	* Used to specify whether to aggregate the source site:   
	  * True: Aggregate the source site, not the field used for counting
	  * False: Do not aggregate the source site, it is the field used for counting.
#### SiteAggregated
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty, input is optional. Default value is True, options include True and False
	* Used to specify whether to aggregate sites:
	  * True: aggregate sites, not used for counting column
	  * False: do not aggregate sites, used for counting column.
#### ProductAggregated
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty, input optional. Default value is True, options include True and False
	* Used to specify whether to aggregate products:
	  * True: aggregate products, not a column for counting
	  * False: do not aggregate products, is a column for counting.
#### PeriodAggregated
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty, input as optional value, default value is True, options include True,False
	* Used to specify whether to aggregate Periods:   
	  * True: Aggregate Periods,not the field for counting
	  * False: Do not aggregate Periods,it is the field for counting.
#### LaneAggregated
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty, input is optional,default value is True,options include True,False
	* Used to specify whether to aggregate transport lanes:   
	  * True: Aggregate transport lanes,not a field for counting
	  * False: Do not aggregate transport lanes,it is a field for counting.
#### ConstraintType
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,no default value,options include Min,Max,Fixed,CondMin
	* Used to specify the type of transport lane count limit:
	* Min: The number of lanes must be greater than or equal to the constraint value
	* Max: The number of lanes must be less than or equal to the constraint value
	* Fixed: The number of lanes must be equal to the constraint value
	* CondMin: The number of lanes can be 0,if not 0,it must be greater than or equal to the constraint value.
#### ConstraintValue
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Indicates the number of lanes under the Constraint type.
#### Status
* **Applicable Algorithms**: OA

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the transport line count limit is involved in model optimization:   
	  * Include: The transport line count limit is involved in model calculation
	  * Exclude: The transport line count limit is not involved in model calculation,and the model will not consider the transport line count limit.
#### Notes
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive statement about the transport line count limit,not involved in model calculation.
#### Custom1
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the transport line count limit,which is convenient for understanding and filtering and does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: OA

* **Description**:
	* Can be empty,no default value
	* Indicates any other custom information about the transport line count limit,which is convenient for understanding and filtering and does not participate in model calculation.

_ _ _

### EndToEndServiceConstraints
#### SourceName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Sites defined in the Site table and their groups (Site Type is \*Facility).
	* Indicates the source Site for transporting the Product.
#### CustomerName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the drop-down box options are Customer (Site Type=Customer) defined in the Site table and groups composed of Customers
	* Indicates the Customer or Customer group to which the end-to-end service Constraint applies.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the drop-down box options are the products defined in the Product table and the groups they form
	* Indicates the product or product group to which the end-to-end service Constraint applies.
#### MaxLeadTime
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the maximum lead time from SourceSite to Customer.
#### Distance
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the maximum transportation distance from SourceSite to Customer.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Include,options include Include,Exclude
	* Used to specify whether end-to-end service Constraints participate in model optimization
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about service limitations,not included in model calculations.

_ _ _

### InterFacilitiesDistanceConstraints
#### MinDistance
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Used when selecting candidate warehouse, the shortest distance that is allowed in model between the two warehouse that are opened
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the inter-site distance Constraint table,which does not participate in model calculation.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the inter-site distance Constraint table,which does not participate in model calculation.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default Include
	* Indicates whether this Constraint is effective
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Indicates the Period Name during which this Constraint is effective
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Identifies the Site Name that this Constraint applies to
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the inter-site distance Constraint table,which does not participate in model calculation.

_ _ _

### DemandEqualRatioConstraints
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of demand sharing constraints,which is not involved in model calculations.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of demand sharing constraints,which is not involved in model calculations.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is Include,options include Include,Exclude
	* Used to specify whether the demand equalization Constraint participates in the model calculation:
	  * Include: participates in the model calculation
	  * Exclude: does not participate in the model calculation
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Used to define the Period range for demand equalization
#### ConstraintBasis
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Quantity,the drop-down box options include: Quantity,Weight,Volume,Value,Price
	* Indicates that the optional measurement units for splitting orders include quantity,weight,volume,value,price
#### PeriodAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, the default value is True, drop-down box options include: True, False
	* For a dimension to be equalized, the dimension must be a Set group, and whether to aggregate is False.
	* Indicates whether to consider multi-period aggregated equalization when demand equalization is applied.
#### SourceAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, the default value is True, drop-down box options include: True, False
	* For a dimension to be equalized, the dimension must be a Set group, and whether to aggregate is False.
	* Indicates whether to consider multi-source aggregated equalization when demand equalization is applied.
#### CustomerAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, the default value is False, drop-down box options include: True, False
	* For a dimension to be equalized, the dimension must be a Set group, and whether to aggregate is False.
	* Indicates whether to consider multi-coustomer aggregated equalization when demand equalization is applied.
#### ServicePeriodAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, the default value is True, drop-down box options include: True, False
	* For a dimension to be equalized, the dimension must be a Set group, and whether to aggregate is False.
	* Indicates whether to consider multi-service-period aggregated equalization when demand equalization is applied.
#### ProductAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, the default value is True, drop-down box options include: True, False
	* For a dimension to be equalized, the dimension must be a Set group, and whether to aggregate is False.
	* Indicates whether to consider multi-products aggregated equalization when demand equalization is applied.
#### SourceName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Used to define the starting range of the demand distribution
#### CustomerName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Used to define the Customer range for demand distribution
#### ServicePeriod
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Used to define the range of the service period for demand equalization
#### OrderScope
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is ConsideredOrders,dropdown options include: ConsideredOrders,TotalOrders
	* Indicates the scope of orders considered when calculating the ratio in case of evenly divided demand
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Used to define the product range for demand distribution
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of demand sharing constraints,which is not involved in model calculations.

_ _ _

### ProductionProcessCountConstraints
#### TotalConstraintsPenalty
* **Applicable Algorithms**: NO

* **Description**:
	* Optional, no default value
	* Expression names must be unique
	This is an optional name for the production process count constraint. The expression created by the production process count constraint can be used in the following ways:
	Create expression constraints by specifying expressions for the values of Expression 1 or Expression 2, allowing combination constraints.
	Create expression-based costs by using the defined expression names in the 'Expression Costs' table, allowing the definition of fixed and variable costs resulting from the constraints.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about the production process count constraint,which does not participate in model calculation.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about the production process count constraint,which does not participate in model calculation.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include
	* Used to specify whether this Constraint participates in model optimization.
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Used to specify the Period to which this Constraint applies.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Used to specify the Site to which this Constraint applies
#### ConstraintValue
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates the limit amount specified by this Constraint
#### ConstraintType
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Optional options include Min,Max,Fixed,CondMin,Define
	* Used to specify the type of production process count constraint:   
	  * Min: The count quantity must be greater than or equal to the constraint value
	  * Max: The count quantity must be less than or equal to the constraint value
	  * Fixed: The count quantity must be equal to the constraint value
	  * CondMin: The count quantity can be 0,if not 0,it must be greater than or equal to the constraint value
	  * Define: Used to create an expression,no constraint value is required
#### IsSoftConstraint
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is False
	* Indicates whether the Constraint is a hard constraint or a soft constraint. Hard constraints must be met,while soft constraints may not be met,but an additional constraint penalty cost must be paid.
#### PeriodAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is True
	* Input options include True and False, which are used to specify whether to aggregate Period
	  * True: Period will be aggregated, hence will not participate in counting
	  * False: Period will not be aggregated, hence will participate in counting.
#### SiteAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, input is optional. Default value is True, options include True and False
	* Used to specify whether to aggregate sites:
	  * True: aggregate sites, not used for counting column
	  * False: do not aggregate sites, used for counting column.
#### ProcessAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is True
	* Input options include True and False, which are used to specify whether to aggregate Production Process
	  * True: Process will be aggregated, hence will not participate in counting
	  * False: Process will not be aggregated, hence will participate in counting.
#### ProductAggregated
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* Default value is True
	* Input options include True and False, which are used to specify whether to aggregate Product
	  * True: Product will be aggregated, hence will not participate in counting
	  * False: Product will not be aggregated, hence will participate in counting.
#### UnitConstraintPenaltyCost
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 1.0
	* Indicates the unit penalty cost for the part where the production process count exceeds the production process count constraint.
#### ProcessName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* No default value
	* Options in the dropdown list are the Production Processes defined by the Production Process table and their composed groups
	* Defines the applicable Production Process for the Production Process Count Constraints,
	  * If 'Individual' group is selected, the constraint will be applied respectively on each member of the individual group. 
	  * If 'Set' group is selected, the constraint will be applied collectively on the set group as a whole.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* Used to specify the Product to which this Constraint applies
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about the production process count constraint,which does not participate in model calculation.

_ _ _

## Advanced Cost
### ExpressionBasedCost
#### Name
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, no default value, the expression cost name must be unique and cannot have the same name as the expression group
	* Indicates the name of the expression cost.
#### Expression
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value,input in the drop-down box,the drop-down box options include expressions defined by the Constraint type Define in the Constraint tables such as model production Constraint,production process Constraint,inventory Constraint,flow Constraint,etc.
	* Indicates the defined expression corresponding to the expression cost.
#### FixedCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is 0
	* Indicates the fixed cost applied to the expression,the input value can be a single value or a Step cost.   
	* Its usage is the same as that in the Site table.
#### FixedCostType
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is IncludeZero, dropdown options include:
	  * IncludeZero: Fixed cost first step applies to output values including zero,i.e.,fixed cost is incurred even when the output value is 0.
	  * ExcludeZero: Conversely, no fixed cost is incurred when the output value is 0.
#### VariableCost
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, default value is 0.
	* Indicates the variable cost which applies to quantity, or weight, or volume defined by the expression. A tiered cost can be set in this field using Tiered Cost Editor.
#### VariableCostType
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, the default value is "All"
	* The drop-down list includes options: 
	* All: The cost will be calculated once based on the tier that the total volume falls in, for example (5000,1.5),(10000,1.25). When the output is 8000, the cost should be 8000\*1.25=10,000.
	* Incremental: The unit cost will be calculated based on the each tier discretely. In the above example, when the output is 8000, the cost should be 5000*1.5+(8000-5000)*1.25=11,250.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the expression cost participates in model optimization:   
	  * Include: participate in model calculation  
	  * Exclude: do not participate in model calculation
#### CostType
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty, no default value.
	* Users can name the cost type according to the actual cost item of the expressions, and BI will split according to the defined cost type.
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive statement about the cost of the expression,which does not participate in the model calculation.

_ _ _

### CarbonOffset
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* The options in the drop-down menu include ALL_SITES,ALL_SITES_SET,user-defined Site groups,and non-Customer type data in the Site table
	* When selecting a group such as ALL_SITES,if the group contains Customer type Sites,such Customer Sites will not take effect,and only the costs of Facility type Sites will be generated.
#### InitialCarbonOffset
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, default value 0.0, unit in tons.
	* Used to define the initial carbon emission allocation for the beginning of the model period.
#### UnitCarbonCost
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, default value 0.0.
	* Used to define the per-ton cost of carbon tax.
#### CarbonOffsetPurchasePrice
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value 0.0
	* Used to define the cost per ton of purchasing carbon credits during carbon trading.
#### CarbonOffsetSalesPrice
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value 0.0
	* Used to define the sales revenue per ton of carbon credits during carbon trading.
#### MinimumEndingCarbonOffset
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, default value is 0.0
	* Defines the lower limit of the target carbon credit balance at the end of the model period.
#### MaximumEndingCarbonOffset
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 0.0
	* Defines the upper limit of the target carbon credit balance at the end of the model period.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include
	* The drop-down box options are Include,Exclude
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value. Does not participate in model calculation
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value. Does not participate in model calculation
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value. Does not participate in model calculation

_ _ _

### CarbonOffsetMultiPeriod
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty
	* The drop-down menu options include ALL_PERIODS,user-defined groups (not Set) of type PERIODS,and data in the Period table other than END
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,no default value
	* The options in the drop-down menu include ALL_SITES,ALL_SITES_SET,user-defined Site groups,and non-Customer type data in the Site table
	* When selecting a group such as ALL_SITES,if the group contains Customer type Sites,such Customer Sites will not take effect,and only the costs of Facility type Sites will be generated.
#### AdditionCarbonOffset
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 0.0,unit is tons
	* Used to define the initial allocation of carbon emission credits at the start of the model period.
#### UnitCarbonCost
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, default value is 0.0
	* Used to define the cost per ton of carbon.
#### CarbonOffsetPurchasePrice
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, default value is 0.0
	* Used to define the cost per ton of purchasing carbon credits during carbon trading within the period.
#### CarbonOffsetSalesPrice
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty, default value is 0.0
	* Used to define the sales revenue per ton of carbon credits during carbon trading within the period.
#### MinimumEndingCarbonOffset
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 0.0
	* Defines the lower limit of the target carbon credit balance within the period.
#### MaximumEndingCarbonOffset
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,default value is 0.0
	* Defines the upper limit of the target carbon credit balance within the period.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include
	* The drop-down box options are Include,Exclude
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Cannot be empty,the default value is Include
	* The drop-down box options are Include,Exclude
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value. Does not participate in model calculation
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value. Does not participate in model calculation

_ _ _

### Rate
#### RateName
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, no default value
	* Indicates the rate name, such as "9 meters 6 rate", "12 meters 5 rate", etc.
#### FixedCost
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,default value is 0
	* Indicates the fixed cost of each route
#### PerDistanceCost
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty
	* Default value is 0. Unit: currency per kilometer. The unit of cost can be customized, but must be consistent within a single model.
	* Indicates the cost per kilometer when the vehicle is not empty (i.e., carrying goods with pending shipment). The cost per kilometer when empty must be defined in the 'per_reposition_distance_cost' field.
#### PerRepositionDistanceCost
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty
	* Default value is 0, unit: currency per kilometer. The unit of cost can be customized, but must be consistent within a single model.
	* Indicates the cost per kilometer when the vehicle is empty (i.e., without goods, on the way to pick up goods, or returning to the Asset Domicile). The non-empty cost per kilometer must be defined in the 'per_distance_cost' field. Typically, the empty and non-empty costs per kilometer are set to be equal.
#### UnitCostBasis
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is Weight, other options include Volume and Quantity
	* Defines the calculation basis for calculating Per Unit Cost of each record in Rate table
#### DiscountRate
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value,it is recommended to fill in a decimal between 0 and 1.
	* Indicates an overall discount on the transport rate, equivalent to multiplying the fixed cost, unit distance (idle) cost, working time cost, transport volume cost, stopover cost, overnight cost, and unit driving (waiting, service) time cost by the discount rate.
#### Status
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the Customer order participates in model optimization,Include means participating in model calculation,Exclude means not participating.
#### Notes
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the shipping rate,which is easy to understand and filter,and is not involved in the model calculation.
#### DutyTimeCost
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty
	* Default value is 0, unit is cost per hour, cost unit can be customized, but each model must be consistent
	* Indicates the corresponding hourly cost of the Asset ID in the working Status, the working Status includes waiting, driving, loading and unloading, and the working time is calculated from the first transportation or loading and unloading (not waiting) operation of the Asset ID.
#### PerUnitCost
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,default value is 0
	* Represents the unit cost per transport volume, with the unit being dollars per unit (Weight-kg,Volume-cubic meters,Quantity-pieces). Assuming that a Shipment Volume is 5 cubic meters and the unit transport cost is 10 dollars per cubic meter, with the transport volume cost calculation based on Volume (Volume), the corresponding transport cost for that Shipment is 10*5=50 dollars.
#### InTransitStopCost
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,default value is 0
	* Indicates the cost incurred at each transit site (excluding asset domicile), unit is cost per (transit point). If an Asset ID performs multiple shipments during its stay at a site, or has both unloading and loading operations, it is still counted as one transit point. However, if the Asset ID shows behavior of arriving at a site -> leaving the site to go to other sites -> returning to the same site, then this site will be considered as transited twice.
#### FixedRestTimeCost
* **Applicable Algorithms**: TO

* **Description**:
	* This field cannot be empty. The default value is 0. The unit is dollars(or other currency) per overnight stay. 
	* Indicates the cost incurred per overnight stay, such as accommodation costs, etc.
	* Not yet effective.
#### FixedAssetCost
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,default value is 0,cost unit can be customized,but each model must be consistent
	* Indicates the fixed cost corresponding to one trip of Asset Id (starting from the starting point of Asset Id and returning to the starting point is one trip). This fixed cost is different from the fixed cost definition in the Asset table. 
	
	The fixed cost in the Asset table is not charged by Route,but calculated by Asset Id. Even if a vehicle runs multiple routes,it is only counted once.
#### MinimumCost
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty,no default value
	* Represents the minimum cost per trip, in dollars. If set to 500, then if the total cost of a certain route derived from other calculation logic is less than 500 dollars, the total cost for that trip will be calculated as 500 dollars.
#### VariableInTransitLoadingStopCost
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty. No default value.
	* Represents the cost incurred at each stop where loading operations are performed (excluding the assets domicile). If an asset picks up multiple orders at one stop, it counts as one loading stop. However, if the asset loads at a stop, leaves for another stop, and then returns to load again, that stop is counted as two loading stops.
	* Step cost input is required, and the step cost rule is incremental, for example, (0,1), (200,2), (300,4). This indicates that:
	  * When the number of loading stops is 1, the cost is 0.
	  * When the number of loading stops is 2, the cost is 200 (an additional 200 on top of the cost for 1 loading stop).
	  * When the number of loading stops is 3, the cost is 400 (an additional 200 on top of the cost for 2 loading stops).
	  * When the number of loading stops is 4, the cost is 700 (an additional 300 on top of the cost for 3 loading stops).
	  * When the number of loading stops exceeds 4 by XX (XX being a positive integer), the cost is 700 + 300XX.
	* If linear cost needs to be expressed, for example, a cost of 500 for each loading stop, you can input (500,1).
#### VariableInTransitUnloadingStopCost
* **Applicable Algorithms**: TO

* **Description**:
	* Can be empty. No default value.
	* Represents the cost incurred at each stop where unloading operations are performed (excluding the assets domicile). If an asset unloads multiple orders at one stop, it counts as one unloading stop. However, if the asset unloads at a stop, leaves for another stop, and then returns to unload again, that stop is counted as two unloading stops.
	* Step cost input is required, and the step cost rule is incremental, for example, (0,1), (200,2), (300,4). This indicates that:
	  - When the number of unloading stops is 1, the cost is 0.
	  - When the number of unloading stops is 2, the cost is 200 (an additional 200 on top of the cost for 1 unloading stop).
	  - When the number of unloading stops is 3, the cost is 400 (an additional 200 on top of the cost for 2 unloading stops).
	  - When the number of unloading stops is 4, the cost is 700 (an additional 300 on top of the cost for 3 unloading stops).
	  - When the number of unloading stops exceeds 4 by X (X being a positive integer), the cost is 700 + 300X.
	* If linear cost needs to be expressed, for example, a cost of 500 for each unloading stop, you can input (500,1).
#### ServiceTimeCost
* **Applicable Algorithms**: TO

* **Description**:
	 * Cannot be empty. Default value is 0, with units of dollars per hour. Cost units can be customized, but must remain consistent within a single model. 
	* Represents the cost per hour associated with the Asset ID being in service (i.e., loading/unloading).                                                                                                                   
#### DriveTimeCost
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty, default value is 0, unit is dollars per hour, cost unit can be customized, but must remain consistent within a single model.
	* Represents the cost per hour associated with the Asset ID being in driving mode.        
#### WaitTimeCost
* **Applicable Algorithms**: TO

* **Description**:
	* Cannot be empty,the default value is 0,the unit is RMB per hour,the cost unit can be customized,but each model must be consistent
	* Indicates the cost per hour corresponding to the Asset Id in the waiting status.

_ _ _

## Network Costing
### BOMTransaction
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the network costing table for easy understanding and screening,and does not participate in model calculation.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the network costing table for easy understanding and screening,and does not participate in model calculation.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,default value is Include,options include Include and Exclude
	* Used to specify whether the network costing order participates in model optimization,Include means participating in model calculation,Exclude means not participating.
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the network costing table for easy understanding and screening,and does not participate in model calculation.
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Used to represent the period name corresponding to BOM transaction in network costing.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Site Name used to restore BOM production volume in network costing
#### BomName
* **Applicable Algorithms**: NO

* **Description**:
	* Used to represent the BOM name corresponding to BOM transaction in network costing.
#### Quantity
* **Applicable Algorithms**: NO

* **Description**:
	* Used to represent the BOM production quantity in network costing
#### BomProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Used to represent the BOM product name corresponding to BOM transaction in network costing.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Product Name used to restore BOM production volume in network costing

_ _ _

### ProductionTransaction
#### Quantity
* **Applicable Algorithms**: NO

* **Description**:
	* Used to represent the amount of production in network costing
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Product Name Used to represent the production volume in network costing
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Site Name Used to represent the production volume in network costing
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Period Name Used to represent the production volume in network costing
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about network costing production volume,which is not involved in model calculation.
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about network costing production volume,which is not involved in model calculation.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Status Used to represent the production volume in network costing
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about network costing production volume,which is not involved in model calculation.

_ _ _

### ProductionProcessTransaction
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Product Name Used to represent the production process volume in network costing
#### ProcessName
* **Applicable Algorithms**: NO

* **Description**:
	* The process name used to represent the production process volume in the network costing
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Site Name Used to represent the production process volume in network costing
#### Quantity
* **Applicable Algorithms**: NO

* **Description**:
	* Used to represent the number of production processes in network costing
#### ProcessStep
* **Applicable Algorithms**: NO

* **Description**:
	* The name of the process step used to represent the production process volume in the network costing
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Period Name used to represent the production process volume in network costing
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the network costing production process volume,which does not participate in the model calculation.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Status Used to represent the production process volume in network costing
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the network costing production process volume,which does not participate in the model calculation.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the network costing production process volume,which does not participate in the model calculation.

_ _ _

### FlowTransaction
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Status Used to represent the flow volume in network costing
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about network costing,not involved in model calculations.
#### Quantity
* **Applicable Algorithms**: NO

* **Description**:
	* Used to represent the amount of flow in network costing
#### ModeName
* **Applicable Algorithms**: NO

* **Description**:
	* Used to represent the transportation mode name corresponding to flow transaction in network costing.
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Product Name Used to represent the flow volume in network costing
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about network costing,not involved in model calculations.
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about network costing,not involved in model calculations.
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Site Name Used to represent the flow volume in network costing
#### SourceName
* **Applicable Algorithms**: NO

* **Description**:
	* Used to represent the starting point name of the flow volume in network costing
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Period Name Used to represent the flow volume in network costing

_ _ _

### InventoryTransaction
#### PeriodName
* **Applicable Algorithms**: NO

* **Description**:
	* Period Name Used to represent the inventory in network costing
#### ProductName
* **Applicable Algorithms**: NO

* **Description**:
	* Product Name Used to represent the inventory in network costing
#### Custom2
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the network costing inventory,which is not involved in the model calculation.
#### Notes
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the network costing inventory,which is not involved in the model calculation.
#### Quantity
* **Applicable Algorithms**: NO

* **Description**:
	* Used to represent the inventory quantity in network costing
#### Custom1
* **Applicable Algorithms**: NO

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the network costing inventory,which is not involved in the model calculation.
#### Status
* **Applicable Algorithms**: NO

* **Description**:
	* Status Used to represent the inventory in network costing
#### SiteName
* **Applicable Algorithms**: NO

* **Description**:
	* Site Name Used to represent the inventory in network costing

_ _ _

## Data Group
### GroupMembers
#### GroupName
* **Applicable Algorithms**: All

* **Description**:
	* Cannot be empty, no default value
	* Indicates the name of a user-defined group. A group contains one or more members. The corresponding relationship between groups and members is defined in the group member table.
#### GroupMembers
* **Applicable Algorithms**: All

* **Description**:
	* Cannot be empty,no default value
	* indicates the members in the group

_ _ _

### Groups
#### Notes
* **Applicable Algorithms**: All

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive description of the group,which does not participate in model calculations.
#### GroupName
* **Applicable Algorithms**: All

* **Description**:
	* Cannot be empty, no default value
	* Represents the name of the group
	* There are three ways to create a new group: 
	  1. Use the New Group button in the group interface to enter the group name, 
	  2. Use the "Add to Group" function button above the model element table to create a group. Taking the Site table as an example, select a few rows and add them to the existing group, or create a new Site group. If you create a new group, you can enter the group name, 
	  3. Export the group and group member table through the background. The group names in the two tables need to match.
#### GroupType
* **Applicable Algorithms**: All

* **Description**:
	* Cannot be empty, no default value, options include Individual and Set
	* Indicates the type of group.
#### GroupEntity
* **Applicable Algorithms**: All

* **Description**:
	* Cannot be empty,no default value,options are Product Name (Product),Site Name (Site) and other table name fields
	* In the Scatlas interface,it is called "group field",and in the exported Excel table,it is called "group entity" 
	* Indicates which field in which table the group members come from

_ _ _

## Transaction Data Forecast
### SiteProductLifeCycle
#### Custom2
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the SiteProduct life period,which does not participate in model calculations.
#### Custom1
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the SiteProduct life period,which does not participate in model calculations.
#### Status
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty; input is optional.
	* Default value is Include; options are Include and Exclude.
	* Used to specify whether the lifecycle of a specified product at a specified site participates in model optimization.
#### CustomerName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* No default value, the drop-down list includes the Site Names defined in Site table (Site Type = Customer) and their groups (the group type must be Individual)
	* Defines the product life cyle applied for a customer or customer group
#### StartDate
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty, drop-down box to enter the date 
	* Used to identify the start date of the life cycle of a given product for a given customer to improve forecasting accuracy
#### EndDate
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty, drop-down box to enter the date 
	* Used to identify the end-of-life date of a given product for a given customer to improve forecasting accuracy
#### ProductName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* No default value, the drop-down list includes the Product Names defined in Product table and their groups (the group type must be Individual)
	* Defines the product life cyle applied for a product or product group
#### Notes
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the SiteProduct life period,which does not participate in model calculations.

_ _ _

### ForecastModelParameters
#### Custom2
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the prediction model parameters,which does not participate in the model calculation.
#### Custom1
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the prediction model parameters,which does not participate in the model calculation.
#### SubmodelName
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty, no default value
	* Used to distinguish different combinations of Site and Product in the forecast scenario
#### Status
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,default value is Include,options include Include,Exclude
	* Used to specify whether the prediction parameter participates in model prediction:   
	  * Include: participates in model prediction   
	  * Exclude: does not participate in model prediction
#### SiteName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,drop-down box selection,drop-down box options are Customer (Site Type = Customer) defined in the Site table and groups composed of Customers
	* Indicates the Customer or Customer group required for the prediction model parameters
#### ForecastHorizon
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* No default value
	* Indicates the value of the period to be predicted when forecasting
#### ForecastStartDate
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,if empty,the Forecast Start Date is the model Period Start Date
	* Select the date in the drop-down box
#### ProductName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Products defined in the Product table and their groups
	* Indicates the Product that needs to be predicted.
#### Notes
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the prediction model parameters,which does not participate in the model calculation.

_ _ _

### RegressorSeries
#### Custom2
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the impact factor sequence,which does not participate in the model calculation.
#### Custom1
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the impact factor sequence,which does not participate in the model calculation.
#### Status
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the regressor participates in model prediction:
#### RegressorName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty, select from the drop-down box, the drop-down box options are the regressors in the regressor definition table
#### Value
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* No default value
	* Defines the value of the Regressor Series at the certain date
#### Date
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* No default value, need to select a data in the drop-down box, the data must be no later than Forecast Start Date 
	* Defines the date that the forecast Regressor Series take effective
#### Notes
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the impact factor sequence,which does not participate in the model calculation.

_ _ _

### RegressorsAssignment
#### Custom2
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the impact factor assignment,which is not involved in the model calculation.
#### Custom1
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the impact factor assignment,which is not involved in the model calculation.
#### Status
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,input is optional
	* The default value is Include,and the options include Include and Exclude
	* Used to specify whether the impact factor allocation participates in the model optimization within the Period
#### SiteName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* Drop-down box selection,the drop-down box options are Customer (Site Type=Customer) defined in the Site table and groups composed of Customers
	* Indicates the Customer or Customer group affected by the regressor
#### RegressorName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* Select from the drop-down box. The drop-down box options are the regressors defined in the regressor definition table.
#### ProductName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the products defined in the Product table and their groups
	* Indicates the product that the specified impact factor will affect
#### Notes
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive information about the impact factor assignment,which is not involved in the model calculation.

_ _ _

### RegressorsDefinition
#### Custom2
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the impact factor definition,which does not participate in the model calculation.
#### Custom1
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the impact factor definition,which does not participate in the model calculation.
#### Status
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,input is optional
	* The default value is Include,and the options include Include and Exclude
	* Used to specify whether the regressor definition participates in the model optimization within the Period
#### RegressorName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty, no default value
	* The name of the regressor can be non-unique
	* Used to name different regressors in the forecast model, such as promotion,sales target,etc.
#### SalesCorrelation
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,default value is Auto, Dropdown options are Auto,Increase,Decrease.
#### MissingValueHandling
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* Default value is Zero, drop-down list includes Zero, One, LastValue, Interpolation
	* Defines the method to fill in the missing value if the value is missed in the middle of a time series
#### Notes
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the impact factor definition,which does not participate in the model calculation.

_ _ _

### Regressors
#### Custom2
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the impact factor,which is not involved in the model calculation.
#### Custom1
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the impact factor,which is not involved in the model calculation.
#### Status
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,default value is Include,options include Include,Exclude
	* Used to specify whether the impact factor participates in model prediction
	  * Include: Participate in model prediction   
	  * Exclude: Do not participate in model prediction
#### SiteName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,drop-down box selection,drop-down box options are Customer (Site Type = Customer) defined in the Site table and groups composed of Customers
	* Indicates the Customer or Customer group affected by the regressor
#### SalesCorrelation
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,default value is Auto,dropdown menu options are Auto,Increase,Decrease
#### FeatureName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty, no default value
	* The name of the regressor, does not have to be unique
	* Used to name different regressor in the forecast model, such as promotion, sales target, etc.
#### Value
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* No default value
	* Defines the value of the Regressor at the certain date
#### Date
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* No default value, need to select a data in the drop-down box, the data must be no later than Forecast Start Date 
	* Defines the date that the forecast Regressor take effective
#### MissingValueHandling
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* Default value is Zero, drop-down box options include: Zero, One, LastValue, Interpolation
	* Indicates the treatment of missing values when the impact factor is not continuous in date
#### ProductName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the products defined in the Product table and their groups
	* Indicates the product that the specified impact factor will affect
#### Notes
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the impact factor,which is not involved in the model calculation.

_ _ _

### DemandOutlier
#### Custom2
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about the exception requirement,which does not participate in the model calculation.
#### Custom1
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description about the exception requirement,which does not participate in the model calculation.
#### Status
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,the default value is Include,options include Include,Exclude
	* Used to specify whether the abnormal demand participates in model prediction:   
	  * Include: Participate in model prediction   
	  * Exclude: Do not participate in model prediction
#### Date
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty, enter the date in the drop-down box
	* Used to identify abnormal demand of Customer and Product on the input date to improve the prediction accuracy
#### CustomerName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty
	* Drop-down box selection,the drop-down box options are Customer (Site Type=Customer) defined in the Site table and groups composed of Customers
	* Indicates the Customer or Customer group affected by the abnormal demand
#### ProductName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the products defined in the Product table and their groups
	* Indicates Products with abnormal requirements
#### Notes
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive description of the abnormal requirement,not involved in the model calculation

_ _ _

### Events
#### Custom2
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the event factor,which does not participate in the model calculation.
#### Custom1
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the event factor,which does not participate in the model calculation.
#### Status
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,default value is Include,options include Include,Exclude
	* Used to specify whether the event factor participates in model prediction:   
	  * Include: Participate in model prediction   
	  * Exclude: Do not participate in model prediction
#### SiteName
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,drop-down box selection,drop-down box options are Customer (Site Type = Customer) defined in the Site table and groups composed of Customers
	* Indicates the Customer or Customer group affected by the event factor
#### EventName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,no default value
	* Used to name different event factors in the forecast model,such as promotions,sales tasks,etc.
#### Date
* **Applicable Algorithms**: FA

* **Description**:
	* Can be left blank, enter the date in the drop-down box
	* Used to identify the sales changes of a product or product group on a specified date to improve the accuracy of the forecast
#### ProximitySales
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,default value is Auto,dropdown options are Auto,Increase,Decrease
	* Auto: The model independently determines the impact of the event feature on the forecast
	* Increase: The event feature has a positive impact on the forecast result
	* Decrease: The event feature has a negative impact on the forecast result
#### ProductName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Products defined in the Product table and their groups
#### Notes
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the event factor,which does not participate in the model calculation.

_ _ _

### SalesPrice
#### Custom2
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive description of the product's price,which is not involved in the model calculation.
#### Custom1
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive description of the product's price,which is not involved in the model calculation.
#### Status
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,default value is Include,options include Include,Exclude
	* Used to specify whether the product price participates in model prediction:  
	  * Include: participate in model prediction   
	  * Exclude: do not participate in model prediction
#### EffectiveDate
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty, enter the date in the drop-down box
	* Used to identify the sales price of a product or product group starting from a specified date
#### CustomerName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,drop-down box selection,drop-down box options are Customer (Site Type = Customer) defined in the Site table and groups composed of Customers
#### Price
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,no default value
	* Enter the product price
	* Provide reference for the forecast algorithm
#### ProductName
* **Applicable Algorithms**: FA

* **Description**:
	* Cannot be empty,no default value,the drop-down box options are the Products defined in the Product table and their groups
#### Notes
* **Applicable Algorithms**: FA

* **Description**:
	* Can be empty,no default value
	* Indicates an optional descriptive description of the product's price,which is not involved in the model calculation.

_ _ _

## Clustering
### ClusteringDimensions
#### ColumnName
* **Applicable Algorithms**: CT

* **Description**:
	* The field name of the backend database,used for the features of decision tree classification
#### Custom1
* **Applicable Algorithms**: CT

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the classification dimension,which does not participate in model calculation.
#### Custom2
* **Applicable Algorithms**: CT

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the classification dimension,which does not participate in model calculation.
#### Status
* **Applicable Algorithms**: CT

* **Description**:
	* Cannot be empty,the default value is Include,optional options include Include,Exclude
	* Used to specify whether the feature participates in the classification algorithm
#### RelativeWeight
* **Applicable Algorithms**: CT

* **Description**:
	* Cannot be empty,the default value is 1
	* Used to specify the weight of this feature in the clustering process
#### TableName
* **Applicable Algorithms**: CT

* **Description**:
	* The table name of the backend database,used to determine the field name of the features of the decision tree classification
#### Notes
* **Applicable Algorithms**: CT

* **Description**:
	* Can be empty,no default value
	* Optional descriptive description of the classification dimension,which does not participate in model calculation.

_ _ _

