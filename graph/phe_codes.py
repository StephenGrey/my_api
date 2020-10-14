"""codes outputed by PHE API"""

#[{row['Area name']:row['Area type']} for k,row in pp.iterrows()]
	
area_types={'Adur': 'ltla', 'Allerdale': 'ltla', 'Amber Valley': 'ltla', 'Arun': 'ltla', 'Ashfield': 'ltla', 'Ashford': 'ltla', 'Aylesbury Vale': 'ltla', 'Babergh': 'ltla', 'Barking and Dagenham': 'utla', 'Barnet': 'utla', 'Barnsley': 'utla', 'Barrow-in-Furness': 'ltla', 'Basildon': 'ltla', 'Basingstoke and Deane': 'ltla', 'Bassetlaw': 'ltla', 'Bath and North East Somerset': 'utla', 'Bedford': 'utla', 'Bexley': 'utla', 'Birmingham': 'utla', 'Blaby': 'ltla', 'Blackburn with Darwen': 'utla', 'Blackpool': 'utla', 'Bolsover': 'ltla', 'Bolton': 'utla', 'Boston': 'ltla', 'Bournemouth, Christchurch and Poole': 'utla', 'Bracknell Forest': 'utla', 'Bradford': 'utla', 'Braintree': 'ltla', 'Breckland': 'ltla', 'Brent': 'utla', 'Brentwood': 'ltla', 'Brighton and Hove': 'utla', 'Bristol, City of': 'utla', 'Broadland': 'ltla', 'Bromley': 'utla', 'Bromsgrove': 'ltla', 'Broxbourne': 'ltla', 'Broxtowe': 'ltla', 'Burnley': 'ltla', 'Bury': 'utla', 'Calderdale': 'utla', 'Cambridge': 'ltla', 'Camden': 'utla', 'Cannock Chase': 'ltla', 'Canterbury': 'ltla', 'Carlisle': 'ltla', 'Castle Point': 'ltla', 'Central Bedfordshire': 'utla', 'Charnwood': 'ltla', 'Chelmsford': 'ltla', 'Cheltenham': 'ltla', 'Cherwell': 'ltla', 'Cheshire East': 'utla', 'Cheshire West and Chester': 'utla', 'Chesterfield': 'ltla', 'Chichester': 'ltla', 'Chiltern': 'ltla', 'Chorley': 'ltla', 'Colchester': 'ltla', 'Copeland': 'ltla', 'Corby': 'ltla', 'Cornwall and Isles of Scilly': 'utla', 'Cotswold': 'ltla', 'County Durham': 'utla', 'Coventry': 'utla', 'Craven': 'ltla', 'Crawley': 'ltla', 'Croydon': 'utla', 'Dacorum': 'ltla', 'Darlington': 'utla', 'Dartford': 'ltla', 'Daventry': 'ltla', 'Derby': 'utla', 'Derbyshire Dales': 'ltla', 'Doncaster': 'utla', 'Dorset': 'utla', 'Dover': 'ltla', 'Dudley': 'utla', 'Ealing': 'utla', 'East Cambridgeshire': 'ltla', 'East Devon': 'ltla', 'East Hampshire': 'ltla', 'East Hertfordshire': 'ltla', 'East Lindsey': 'ltla', 'East Northamptonshire': 'ltla', 'East Riding of Yorkshire': 'utla', 'East Staffordshire': 'ltla', 'East Suffolk': 'ltla', 'Eastbourne': 'ltla', 'Eastleigh': 'ltla', 'Eden': 'ltla', 'Elmbridge': 'ltla', 'Enfield': 'utla', 'Epping Forest': 'ltla', 'Epsom and Ewell': 'ltla', 'Erewash': 'ltla', 'Exeter': 'ltla', 'Fareham': 'ltla', 'Fenland': 'ltla', 'Folkestone and Hythe': 'ltla', 'Forest of Dean': 'ltla', 'Fylde': 'ltla', 'Gateshead': 'utla', 'Gedling': 'ltla', 'Gloucester': 'ltla', 'Gosport': 'ltla', 'Gravesham': 'ltla', 'Great Yarmouth': 'ltla', 'Greenwich': 'utla', 'Guildford': 'ltla', 'Hackney and City of London': 'utla', 'Halton': 'utla', 'Hambleton': 'ltla', 'Hammersmith and Fulham': 'utla', 'Harborough': 'ltla', 'Haringey': 'utla', 'Harlow': 'ltla', 'Harrogate': 'ltla', 'Harrow': 'utla', 'Hart': 'ltla', 'Hartlepool': 'utla', 'Hastings': 'ltla', 'Havant': 'ltla', 'Havering': 'utla', 'Herefordshire, County of': 'utla', 'Hertsmere': 'ltla', 'High Peak': 'ltla', 'Hillingdon': 'utla', 'Hinckley and Bosworth': 'ltla', 'Horsham': 'ltla', 'Hounslow': 'utla', 'Huntingdonshire': 'ltla', 'Hyndburn': 'ltla', 'Ipswich': 'ltla', 'Isle of Wight': 'utla', 'Islington': 'utla', 'Kensington and Chelsea': 'utla', 'Kettering': 'ltla', "King's Lynn and West Norfolk": 'ltla', 'Kingston upon Hull, City of': 'utla', 'Kingston upon Thames': 'utla', 'Kirklees': 'utla', 'Knowsley': 'utla', 'Lambeth': 'utla', 'Lancaster': 'ltla', 'Leeds': 'utla', 'Leicester': 'utla', 'Lewes': 'ltla', 'Lewisham': 'utla', 'Lichfield': 'ltla', 'Lincoln': 'ltla', 'Liverpool': 'utla', 'Luton': 'utla', 'Maidstone': 'ltla', 'Maldon': 'ltla', 'Malvern Hills': 'ltla', 'Manchester': 'utla', 'Mansfield': 'ltla', 'Medway': 'utla', 'Melton': 'ltla', 'Mendip': 'ltla', 'Merton': 'utla', 'Mid Devon': 'ltla', 'Mid Suffolk': 'ltla', 'Mid Sussex': 'ltla', 'Middlesbrough': 'utla', 'Milton Keynes': 'utla', 'Mole Valley': 'ltla', 'New Forest': 'ltla', 'Newark and Sherwood': 'ltla', 'Newcastle upon Tyne': 'utla', 'Newcastle-under-Lyme': 'ltla', 'Newham': 'utla', 'North Devon': 'ltla', 'North East Derbyshire': 'ltla', 'North East Lincolnshire': 'utla', 'North Hertfordshire': 'ltla', 'North Kesteven': 'ltla', 'North Lincolnshire': 'utla', 'North Norfolk': 'ltla', 'North Somerset': 'utla', 'North Tyneside': 'utla', 'North Warwickshire': 'ltla', 'North West Leicestershire': 'ltla', 'Northampton': 'ltla', 'Northumberland': 'utla', 'Norwich': 'ltla', 'Nottingham': 'utla', 'Nuneaton and Bedworth': 'ltla', 'Oadby and Wigston': 'ltla', 'Oldham': 'utla', 'Oxford': 'ltla', 'Pendle': 'ltla', 'Peterborough': 'utla', 'Plymouth': 'utla', 'Portsmouth': 'utla', 'Preston': 'ltla', 'Reading': 'utla', 'Redbridge': 'utla', 'Redcar and Cleveland': 'utla', 'Redditch': 'ltla', 'Reigate and Banstead': 'ltla', 'Ribble Valley': 'ltla', 'Richmond upon Thames': 'utla', 'Richmondshire': 'ltla', 'Rochdale': 'utla', 'Rochford': 'ltla', 'Rossendale': 'ltla', 'Rother': 'ltla', 'Rotherham': 'utla', 'Rugby': 'ltla', 'Runnymede': 'ltla', 'Rushcliffe': 'ltla', 'Rushmoor': 'ltla', 'Rutland': 'utla', 'Ryedale': 'ltla', 'Salford': 'utla', 'Sandwell': 'utla', 'Scarborough': 'ltla', 'Sedgemoor': 'ltla', 'Sefton': 'utla', 'Selby': 'ltla', 'Sevenoaks': 'ltla', 'Sheffield': 'utla', 'Shropshire': 'utla', 'Slough': 'utla', 'Solihull': 'utla', 'Somerset West and Taunton': 'ltla', 'South Bucks': 'ltla', 'South Cambridgeshire': 'ltla', 'South Derbyshire': 'ltla', 'South Gloucestershire': 'utla', 'South Hams': 'ltla', 'South Holland': 'ltla', 'South Kesteven': 'ltla', 'South Lakeland': 'ltla', 'South Norfolk': 'ltla', 'South Northamptonshire': 'ltla', 'South Oxfordshire': 'ltla', 'South Ribble': 'ltla', 'South Somerset': 'ltla', 'South Staffordshire': 'ltla', 'South Tyneside': 'utla', 'Southampton': 'utla', 'Southend-on-Sea': 'utla', 'Southwark': 'utla', 'Spelthorne': 'ltla', 'St Albans': 'ltla', 'St. Helens': 'utla', 'Stafford': 'ltla', 'Staffordshire Moorlands': 'ltla', 'Stevenage': 'ltla', 'Stockport': 'utla', 'Stockton-on-Tees': 'utla', 'Stoke-on-Trent': 'utla', 'Stratford-on-Avon': 'ltla', 'Stroud': 'ltla', 'Sunderland': 'utla', 'Surrey Heath': 'ltla', 'Sutton': 'utla', 'Swale': 'ltla', 'Swindon': 'utla', 'Tameside': 'utla', 'Tamworth': 'ltla', 'Tandridge': 'ltla', 'Teignbridge': 'ltla', 'Telford and Wrekin': 'utla', 'Tendring': 'ltla', 'Test Valley': 'ltla', 'Tewkesbury': 'ltla', 'Thanet': 'ltla', 'Three Rivers': 'ltla', 'Thurrock': 'utla', 'Tonbridge and Malling': 'ltla', 'Torbay': 'utla', 'Torridge': 'ltla', 'Tower Hamlets': 'utla', 'Trafford': 'utla', 'Tunbridge Wells': 'ltla', 'Uttlesford': 'ltla', 'Vale of White Horse': 'ltla', 'Wakefield': 'utla', 'Walsall': 'utla', 'Waltham Forest': 'utla', 'Wandsworth': 'utla', 'Warrington': 'utla', 'Warwick': 'ltla', 'Watford': 'ltla', 'Waverley': 'ltla', 'Wealden': 'ltla', 'Wellingborough': 'ltla', 'Welwyn Hatfield': 'ltla', 'West Berkshire': 'utla', 'West Devon': 'ltla', 'West Lancashire': 'ltla', 'West Lindsey': 'ltla', 'West Oxfordshire': 'ltla', 'West Suffolk': 'ltla', 'Westminster': 'utla', 'Wigan': 'utla', 'Wiltshire': 'utla', 'Winchester': 'ltla', 'Windsor and Maidenhead': 'utla', 'Wirral': 'utla', 'Woking': 'ltla', 'Wokingham': 'utla', 'Wolverhampton': 'utla', 'Worcester': 'ltla', 'Worthing': 'ltla', 'Wychavon': 'ltla', 'Wycombe': 'ltla', 'Wyre': 'ltla', 'Wyre Forest': 'ltla', 'York': 'utla', 'England': 'nation', 'East Midlands': 'region', 'East of England': 'region', 'London': 'region', 'North East': 'region', 'North West': 'region', 'South East': 'region', 'South West': 'region', 'West Midlands': 'region', 'Yorkshire and The Humber': 'region', 'Buckinghamshire': 'utla', 'Cambridgeshire': 'utla', 'Cumbria': 'utla', 'Derbyshire': 'utla', 'Devon': 'utla', 'East Sussex': 'utla', 'Essex': 'utla', 'Gloucestershire': 'utla', 'Hampshire': 'utla', 'Hertfordshire': 'utla', 'Kent': 'utla', 'Lancashire': 'utla', 'Leicestershire': 'utla', 'Lincolnshire': 'utla', 'Norfolk': 'utla', 'North Yorkshire': 'utla', 'Northamptonshire': 'utla', 'Nottinghamshire': 'utla', 'Oxfordshire': 'utla', 'Somerset': 'utla', 'Staffordshire': 'utla', 'Suffolk': 'utla', 'Surrey': 'utla', 'Warwickshire': 'utla', 'West Sussex': 'utla', 'Worcestershire': 'utla', 'Northern Ireland': 'nation', 'Scotland': 'nation', 'Wales': 'nation',
'Antrim and Newtownabbey': 'utla',
'Armagh City, Banbridge and Craigavon': 'utla',
'Belfast': 'utla',
'Causeway Coast and Glens': 'utla',
'Derry City and Strabane': 'utla',
'Fermanagh and Omagh': 'utla',
'Lisburn and Castlereagh': 'utla',
'Mid and East Antrim': 'utla',
'Mid Ulster': 'utla',
'Newry, Mourne and Down': 'utla',
'Ards and North Down': 'utla', 
'Dumfries and Galloway':'utla',
'Isle of Anglesey':'utla',
'Gwynedd':'utla',
'Conwy':'utla',
'Denbighshire':'utla',
'Flintshire':'utla',
'Wrexham':'utla',
'Ceredigion':'utla',
'Pembrokeshire':'utla',
'Carmarthenshire':'utla',
'Swansea':'utla',
'Neath Port Talbot':'utla',
'Bridgend':'utla',
'Vale of Glamorgan':'utla',
'Cardiff':'utla',
'Rhondda Cynon Taf':'utla',
'Caerphilly':'utla',
'Blaenau Gwent':'utla',
'Torfaen':'utla',
'Monmouthshire':'utla',
'Newport':'utla',
'Powys':'utla',
'Merthyr Tydfil':'utla',
'Aberdeen City':'utla',
'Aberdeenshire':'utla',
'Angus':'utla',
'Argyll and Bute':'utla',
'City of Edinburgh':'utla',
'Clackmannanshire':'utla',
'Dumfries and Galloway':'utla',
'Dundee City':'utla',
'East Ayrshire':'utla',
'East Dunbartonshire':'utla',
'East Lothian':'utla',
'East Renfrewshire':'utla',
'Falkirk':'utla',
'Fife':'utla',
'Glasgow City':'utla',
'Highland':'utla',
'Inverclyde':'utla',
'Midlothian':'utla',
'Moray':'utla',
'Na h-Eileanan Siar':'utla',
'North Ayrshire':'utla',
'North Lanarkshire':'utla',
'Orkney Islands':'utla',
'Perth and Kinross':'utla',
'Renfrewshire':'utla',
'Scottish Borders':'utla',
'Shetland Islands':'utla',
'South Ayrshire':'utla',
'South Lanarkshire':'utla',
'Stirling':'utla',
'West Dunbartonshire':'utla',
'West Lothian':'utla',

}

#'S08000019': 'Forth Valley', 'S08000020': 'Grampian', 'S08000022': 'Highland', 'S08000024': 'Lothian', 'S08000025': 'Orkney', 'S08000026': 'Shetland', 'S08000028': 'Western Isles', 'S08000029': 'Fife', 'S08000030': 'Tayside', 'S08000031': 'Greater Glasgow and Clyde', 'S08000032': 'Lanarkshire', 'W06000001': 'Isle of Anglesey', 'W06000002': 'Gwynedd', 'W06000003': 'Conwy', 'W06000004': 'Denbighshire', 'W06000005': 'Flintshire', 'W06000006': 'Wrexham', 'W06000008': 'Ceredigion', 'W06000009': 'Pembrokeshire', 'W06000010': 'Carmarthenshire', 'W06000011': 'Swansea', 'W06000012': 'Neath Port Talbot', 'W06000013': 'Bridgend', 'W06000014': 'Vale of Glamorgan', 'W06000015': 'Cardiff', 'W06000016': 'Rhondda Cynon Taf', 'W06000018': 'Caerphilly', 'W06000019': 'Blaenau Gwent', 'W06000020': 'Torfaen', 'W06000021': 'Monmouthshire', 'W06000022': 'Newport', 'W06000023': 'Powys', 'W06000024': 'Merthyr Tydfil'

#{row['Area name']:row['Area code'] for k,row in pp.iterrows()}

codes={'Adur': 'E07000223', 'Allerdale': 'E07000026', 'Amber Valley': 'E07000032', 'Arun': 'E07000224', 'Ashfield': 'E07000170', 'Ashford': 'E07000105', 'Aylesbury Vale': 'E07000004', 'Babergh': 'E07000200', 'Barking and Dagenham': 'E09000002', 'Barnet': 'E09000003', 'Barnsley': 'E08000016', 'Barrow-in-Furness': 'E07000027', 'Basildon': 'E07000066', 'Basingstoke and Deane': 'E07000084', 'Bassetlaw': 'E07000171', 'Bath and North East Somerset': 'E06000022', 'Bedford': 'E06000055', 'Bexley': 'E09000004', 'Birmingham': 'E08000025', 'Blaby': 'E07000129', 'Blackburn with Darwen': 'E06000008', 'Blackpool': 'E06000009', 'Bolsover': 'E07000033', 'Bolton': 'E08000001', 'Boston': 'E07000136', 'Bournemouth, Christchurch and Poole': 'E06000058', 'Bracknell Forest': 'E06000036', 'Bradford': 'E08000032', 'Braintree': 'E07000067', 'Breckland': 'E07000143', 'Brent': 'E09000005', 'Brentwood': 'E07000068', 'Brighton and Hove': 'E06000043', 'Bristol, City of': 'E06000023', 'Broadland': 'E07000144', 'Bromley': 'E09000006', 'Bromsgrove': 'E07000234', 'Broxbourne': 'E07000095', 'Broxtowe': 'E07000172', 'Burnley': 'E07000117', 'Bury': 'E08000002', 'Calderdale': 'E08000033', 'Cambridge': 'E07000008', 'Camden': 'E09000007', 'Cannock Chase': 'E07000192', 'Canterbury': 'E07000106', 'Carlisle': 'E07000028', 'Castle Point': 'E07000069', 'Central Bedfordshire': 'E06000056', 'Charnwood': 'E07000130', 'Chelmsford': 'E07000070', 'Cheltenham': 'E07000078', 'Cherwell': 'E07000177', 'Cheshire East': 'E06000049', 'Cheshire West and Chester': 'E06000050', 'Chesterfield': 'E07000034', 'Chichester': 'E07000225', 'Chiltern': 'E07000005', 'Chorley': 'E07000118', 'Colchester': 'E07000071', 'Copeland': 'E07000029', 'Corby': 'E07000150', 'Cornwall and Isles of Scilly': 'E06000052', 'Cotswold': 'E07000079', 'County Durham': 'E06000047', 'Coventry': 'E08000026', 'Craven': 'E07000163', 'Crawley': 'E07000226', 'Croydon': 'E09000008', 'Dacorum': 'E07000096', 'Darlington': 'E06000005', 'Dartford': 'E07000107', 'Daventry': 'E07000151', 'Derby': 'E06000015', 'Derbyshire Dales': 'E07000035', 'Doncaster': 'E08000017', 'Dorset': 'E06000059', 'Dover': 'E07000108', 'Dudley': 'E08000027', 'Ealing': 'E09000009', 'East Cambridgeshire': 'E07000009', 'East Devon': 'E07000040', 'East Hampshire': 'E07000085', 'East Hertfordshire': 'E07000242', 'East Lindsey': 'E07000137', 'East Northamptonshire': 'E07000152', 'East Riding of Yorkshire': 'E06000011', 'East Staffordshire': 'E07000193', 'East Suffolk': 'E07000244', 'Eastbourne': 'E07000061', 'Eastleigh': 'E07000086', 'Eden': 'E07000030', 'Elmbridge': 'E07000207', 'Enfield': 'E09000010', 'Epping Forest': 'E07000072', 'Epsom and Ewell': 'E07000208', 'Erewash': 'E07000036', 'Exeter': 'E07000041', 'Fareham': 'E07000087', 'Fenland': 'E07000010', 'Folkestone and Hythe': 'E07000112', 'Forest of Dean': 'E07000080', 'Fylde': 'E07000119', 'Gateshead': 'E08000037', 'Gedling': 'E07000173', 'Gloucester': 'E07000081', 'Gosport': 'E07000088', 'Gravesham': 'E07000109', 'Great Yarmouth': 'E07000145', 'Greenwich': 'E09000011', 'Guildford': 'E07000209', 'Hackney and City of London': 'E09000012', 'Halton': 'E06000006', 'Hambleton': 'E07000164', 'Hammersmith and Fulham': 'E09000013', 'Harborough': 'E07000131', 'Haringey': 'E09000014', 'Harlow': 'E07000073', 'Harrogate': 'E07000165', 'Harrow': 'E09000015', 'Hart': 'E07000089', 'Hartlepool': 'E06000001', 'Hastings': 'E07000062', 'Havant': 'E07000090', 'Havering': 'E09000016', 'Herefordshire, County of': 'E06000019', 'Hertsmere': 'E07000098', 'High Peak': 'E07000037', 'Hillingdon': 'E09000017', 'Hinckley and Bosworth': 'E07000132', 'Horsham': 'E07000227', 'Hounslow': 'E09000018', 'Huntingdonshire': 'E07000011', 'Hyndburn': 'E07000120', 'Ipswich': 'E07000202', 'Isle of Wight': 'E06000046', 'Islington': 'E09000019', 'Kensington and Chelsea': 'E09000020', 'Kettering': 'E07000153', "King's Lynn and West Norfolk": 'E07000146', 'Kingston upon Hull, City of': 'E06000010', 'Kingston upon Thames': 'E09000021', 'Kirklees': 'E08000034', 'Knowsley': 'E08000011', 'Lambeth': 'E09000022', 'Lancaster': 'E07000121', 'Leeds': 'E08000035', 'Leicester': 'E06000016', 'Lewes': 'E07000063', 'Lewisham': 'E09000023', 'Lichfield': 'E07000194', 'Lincoln': 'E07000138', 'Liverpool': 'E08000012', 'Luton': 'E06000032', 'Maidstone': 'E07000110', 'Maldon': 'E07000074', 'Malvern Hills': 'E07000235', 'Manchester': 'E08000003', 'Mansfield': 'E07000174', 'Medway': 'E06000035', 'Melton': 'E07000133', 'Mendip': 'E07000187', 'Merton': 'E09000024', 'Mid Devon': 'E07000042', 'Mid Suffolk': 'E07000203', 'Mid Sussex': 'E07000228', 'Middlesbrough': 'E06000002', 'Milton Keynes': 'E06000042', 'Mole Valley': 'E07000210', 'New Forest': 'E07000091', 'Newark and Sherwood': 'E07000175', 'Newcastle upon Tyne': 'E08000021', 'Newcastle-under-Lyme': 'E07000195', 'Newham': 'E09000025', 'North Devon': 'E07000043', 'North East Derbyshire': 'E07000038', 'North East Lincolnshire': 'E06000012', 'North Hertfordshire': 'E07000099', 'North Kesteven': 'E07000139', 'North Lincolnshire': 'E06000013', 'North Norfolk': 'E07000147', 'North Somerset': 'E06000024', 'North Tyneside': 'E08000022', 'North Warwickshire': 'E07000218', 'North West Leicestershire': 'E07000134', 'Northampton': 'E07000154', 'Northumberland': 'E06000057', 'Norwich': 'E07000148', 'Nottingham': 'E06000018', 'Nuneaton and Bedworth': 'E07000219', 'Oadby and Wigston': 'E07000135', 'Oldham': 'E08000004', 'Oxford': 'E07000178', 'Pendle': 'E07000122', 'Peterborough': 'E06000031', 'Plymouth': 'E06000026', 'Portsmouth': 'E06000044', 'Preston': 'E07000123', 'Reading': 'E06000038', 'Redbridge': 'E09000026', 'Redcar and Cleveland': 'E06000003', 'Redditch': 'E07000236', 'Reigate and Banstead': 'E07000211', 'Ribble Valley': 'E07000124', 'Richmond upon Thames': 'E09000027', 'Richmondshire': 'E07000166', 'Rochdale': 'E08000005', 'Rochford': 'E07000075', 'Rossendale': 'E07000125', 'Rother': 'E07000064', 'Rotherham': 'E08000018', 'Rugby': 'E07000220', 'Runnymede': 'E07000212', 'Rushcliffe': 'E07000176', 'Rushmoor': 'E07000092', 'Rutland': 'E06000017', 'Ryedale': 'E07000167', 'Salford': 'E08000006', 'Sandwell': 'E08000028', 'Scarborough': 'E07000168', 'Sedgemoor': 'E07000188', 'Sefton': 'E08000014', 'Selby': 'E07000169', 'Sevenoaks': 'E07000111', 'Sheffield': 'E08000019', 'Shropshire': 'E06000051', 'Slough': 'E06000039', 'Solihull': 'E08000029', 'Somerset West and Taunton': 'E07000246', 'South Bucks': 'E07000006', 'South Cambridgeshire': 'E07000012', 'South Derbyshire': 'E07000039', 'South Gloucestershire': 'E06000025', 'South Hams': 'E07000044', 'South Holland': 'E07000140', 'South Kesteven': 'E07000141', 'South Lakeland': 'E07000031', 'South Norfolk': 'E07000149', 'South Northamptonshire': 'E07000155', 'South Oxfordshire': 'E07000179', 'South Ribble': 'E07000126', 'South Somerset': 'E07000189', 'South Staffordshire': 'E07000196', 'South Tyneside': 'E08000023', 'Southampton': 'E06000045', 'Southend-on-Sea': 'E06000033', 'Southwark': 'E09000028', 'Spelthorne': 'E07000213', 'St Albans': 'E07000240', 'St. Helens': 'E08000013', 'Stafford': 'E07000197', 'Staffordshire Moorlands': 'E07000198', 'Stevenage': 'E07000243', 'Stockport': 'E08000007', 'Stockton-on-Tees': 'E06000004', 'Stoke-on-Trent': 'E06000021', 'Stratford-on-Avon': 'E07000221', 'Stroud': 'E07000082', 'Sunderland': 'E08000024', 'Surrey Heath': 'E07000214', 'Sutton': 'E09000029', 'Swale': 'E07000113', 'Swindon': 'E06000030', 'Tameside': 'E08000008', 'Tamworth': 'E07000199', 'Tandridge': 'E07000215', 'Teignbridge': 'E07000045', 'Telford and Wrekin': 'E06000020', 'Tendring': 'E07000076', 'Test Valley': 'E07000093', 'Tewkesbury': 'E07000083', 'Thanet': 'E07000114', 'Three Rivers': 'E07000102', 'Thurrock': 'E06000034', 'Tonbridge and Malling': 'E07000115', 'Torbay': 'E06000027', 'Torridge': 'E07000046', 'Tower Hamlets': 'E09000030', 'Trafford': 'E08000009', 'Tunbridge Wells': 'E07000116', 'Uttlesford': 'E07000077', 'Vale of White Horse': 'E07000180', 'Wakefield': 'E08000036', 'Walsall': 'E08000030', 'Waltham Forest': 'E09000031', 'Wandsworth': 'E09000032', 'Warrington': 'E06000007', 'Warwick': 'E07000222', 'Watford': 'E07000103', 'Waverley': 'E07000216', 'Wealden': 'E07000065', 'Wellingborough': 'E07000156', 'Welwyn Hatfield': 'E07000241', 'West Berkshire': 'E06000037', 'West Devon': 'E07000047', 'West Lancashire': 'E07000127', 'West Lindsey': 'E07000142', 'West Oxfordshire': 'E07000181', 'West Suffolk': 'E07000245', 'Westminster': 'E09000033', 'Wigan': 'E08000010', 'Wiltshire': 'E06000054', 'Winchester': 'E07000094', 'Windsor and Maidenhead': 'E06000040', 'Wirral': 'E08000015', 'Woking': 'E07000217', 'Wokingham': 'E06000041', 'Wolverhampton': 'E08000031', 'Worcester': 'E07000237', 'Worthing': 'E07000229', 'Wychavon': 'E07000238', 'Wycombe': 'E07000007', 'Wyre': 'E07000128', 'Wyre Forest': 'E07000239', 'York': 'E06000014', 'England': 'E92000001', 'East Midlands': 'E12000004', 'East of England': 'E12000006', 'London': 'E12000007', 'North East': 'E12000001', 'North West': 'E12000002', 'South East': 'E12000008', 'South West': 'E12000009', 'West Midlands': 'E12000005', 'Yorkshire and The Humber': 'E12000003', 'Buckinghamshire': 'E10000002', 'Cambridgeshire': 'E10000003', 'Cumbria': 'E10000006', 'Derbyshire': 'E10000007', 'Devon': 'E10000008', 'East Sussex': 'E10000011', 'Essex': 'E10000012', 'Gloucestershire': 'E10000013', 'Hampshire': 'E10000014', 'Hertfordshire': 'E10000015', 'Kent': 'E10000016', 'Lancashire': 'E10000017', 'Leicestershire': 'E10000018', 'Lincolnshire': 'E10000019', 'Norfolk': 'E10000020', 'North Yorkshire': 'E10000023', 'Northamptonshire': 'E10000021', 'Nottinghamshire': 'E10000024', 'Oxfordshire': 'E10000025', 'Somerset': 'E10000027', 'Staffordshire': 'E10000028', 'Suffolk': 'E10000029', 'Surrey': 'E10000030', 'Warwickshire': 'E10000031', 'West Sussex': 'E10000032', 'Worcestershire': 'E10000034', 'Northern Ireland': 'N92000002', 'Scotland': 'S92000003', 'Wales': 'W92000004',
'Aberdeen City':'S12000033','Aberdeenshire':'S12000034','Angus':'S12000041','Argyll and Bute':'S12000035','City of Edinburgh':'S12000036','Clackmannanshire':'S12000005','Dumfries and Galloway':'S12000006','Dundee City':'S12000042','East Ayrshire':'S12000008','East Dunbartonshire':'S12000045','East Lothian':'S12000010','East Renfrewshire':'S12000011','Falkirk':'S12000014','Fife':'S12000047','Glasgow City':'S12000049','Highland':'S12000017','Inverclyde':'S12000018','Midlothian':'S12000019','Moray':'S12000020','Na h-Eileanan Siar':'S12000013','North Ayrshire':'S12000021','North Lanarkshire':'S12000050','Orkney Islands':'S12000023','Perth and Kinross':'S12000048','Renfrewshire':'S12000038','Scottish Borders':'S12000026','Shetland Islands':'S12000027','South Ayrshire':'S12000028','South Lanarkshire':'S12000029','Stirling':'S12000030','West Dunbartonshire':'S12000039','West Lothian':'S12000040'

}


#
#
#INFO [api.graph.phe_fetch:285] Fetching Ayrshire and Arran
#[26/Sep/2020 06:29:58] ERROR [api.graph.phe_fetch:298] No data here
#[26/Sep/2020 06:29:58] INFO [api.graph.phe_fetch:285] Fetching Borders
#[26/Sep/2020 06:29:59] ERROR [api.graph.phe_fetch:298] No data here
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:285] Fetching Dumfries and Galloway
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Forth Valley - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Grampian - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Highland - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Lothian - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Orkney - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Shetland - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Western Isles - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Fife - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Tayside - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Greater Glasgow and Clyde - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Lanarkshire - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Isle of Anglesey - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Gwynedd - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Conwy - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Denbighshire - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Flintshire - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Wrexham - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Ceredigion - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Pembrokeshire - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Carmarthenshire - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Swansea - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Neath Port Talbot - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Bridgend - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Vale of Glamorgan - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Cardiff - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Rhondda Cynon Taf - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Caerphilly - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Blaenau Gwent - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Torfaen - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Monmouthshire - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Newport - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Powys - not in PHE API
#[26/Sep/2020 06:29:59] INFO [api.graph.phe_fetch:280] Not fetching Merthyr Tydfil - not in PHE API
#[26/Sep/2020 06:29:59]