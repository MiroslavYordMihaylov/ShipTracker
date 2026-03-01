colors_dict = {
        # Black Sea Countries
        '207': "\033[92mBG",  # Bulgaria - Green
        '273': "\033[94mRU",  # Russia - Blue
        '213': "\033[0;0mGE",  # Georgia - White/Reset
        '272': "\033[93mUA",  # Ukraine - Yellow
        '271': "\033[91mTR",  # Turkey - Red
        '264': "\033[96mRO",  # Romania - Cyan
        '214': "\033[95mMD",  # Moldova - Purple

        # Mediterranean & Southern Europe
        '215': "\033[92mMT",  # Malta - Green
        '247': "\033[96mIT",  # Italy - Cyan
        '248': "\033[96mIT",  # Italy - Cyan
        '249': "\033[96mIT",  # Italy - Cyan
        '237': "\033[92mGR",  # Greece - Green
        '239': "\033[92mGR",  # Greece - Green
        '240': "\033[92mGR",  # Greece - Green
        '241': "\033[92mGR",  # Greece - Green
        '224': "\033[95mES",  # Spain - Purple
        '225': "\033[95mES",  # Spain - Purple
        '226': "\033[94mFR",  # France - Blue
        '227': "\033[94mFR",  # France - Blue
        '228': "\033[94mFR",  # France - Blue
        '209': "\033[93mCY",  # Cyprus - Yellow
        '210': "\033[93mCY",  # Cyprus - Yellow
        '212': "\033[93mCY",  # Cyprus - Yellow
        '238': "\033[91mHR",  # Croatia - Red
        '278': "\033[96mSI",  # Slovenia - Cyan
        '279': "\033[92mRS",  # Serbia - Green
        '262': "\033[94mME",  # Montenegro - Blue
        '201': "\033[95mAL",  # Albania - Purple
        '202': "\033[93mAD",  # Andorra - Yellow

        # Northern & Western Europe
        '218': "\033[94mDE",  # Germany - Blue
        '211': "\033[92mDE",  # Germany - Green (additional)
        '219': "\033[92mDK",  # Denmark - Green
        '220': "\033[92mDK",  # Denmark - Green
        '221': "\033[96mNO",  # Norway - Cyan
        '222': "\033[96mNO",  # Norway - Cyan
        '223': "\033[96mNO",  # Norway - Cyan
        '230': "\033[95mFI",  # Finland - Purple
        '231': "\033[95mFO",  # Faroe Islands - Purple
        '232': "\033[95mGB",  # United Kingdom - Purple
        '233': "\033[95mGB",  # United Kingdom - Purple
        '234': "\033[95mGB",  # United Kingdom - Purple
        '235': "\033[95mGB",  # United Kingdom - Purple
        '236': "\033[95mGI",  # Gibraltar - Purple
        '244': "\033[93mNL",  # Netherlands - Yellow
        '245': "\033[93mNL",  # Netherlands - Yellow
        '246': "\033[93mNL",  # Netherlands - Yellow
        '250': "\033[96mIE",  # Ireland - Cyan
        '251': "\033[96mIS",  # Iceland - Cyan
        '255': "\033[94mPT",  # Portugal - Blue
        '256': "\033[94mMT",  # Malta - Blue
        '257': "\033[92mNO",  # Norway - Green
        '258': "\033[92mNO",  # Norway - Green
        '259': "\033[92mNO",  # Norway - Green
        '261': "\033[92mPL",  # Poland - Green
        '265': "\033[96mSE",  # Sweden - Cyan
        '266': "\033[96mSE",  # Sweden - Cyan
        '267': "\033[93mSK",  # Slovakia - Yellow
        '268': "\033[93mSM",  # San Marino - Yellow
        '269': "\033[94mCH",  # Switzerland - Blue
        '274': "\033[95mCZ",  # Czech Republic - Purple
        '275': "\033[95mLV",  # Latvia - Purple
        '276': "\033[95mEE",  # Estonia - Purple
        '277': "\033[95mLT",  # Lithuania - Purple

        # North America
        '338': "\033[96mUS",  # USA - Cyan
        '366': "\033[96mUS",  # USA - Cyan
        '367': "\033[96mUS",  # USA - Cyan
        '368': "\033[96mUS",  # USA - Cyan
        '369': "\033[96mUS",  # USA - Cyan
        '316': "\033[91mCA",  # Canada - Red
        '317': "\033[91mCA",  # Canada - Red
        '318': "\033[91mCA",  # Canada - Red
        '319': "\033[91mCA",  # Canada - Red

        # Central America & Caribbean
        '304': "\033[91mAB", #Antigua and Barbuda
        '305': "\033[91mAB", #Antigua and Barbuda
        '301': "\033[93mBS",  # Bahamas - Yellow
        '308': "\033[96mBS",  # Bahamas - Cyan
        '309': "\033[96mBS",  # Bahamas - Cyan
        '311': "\033[96mBS",  # Bahamas - Cyan
        '312': "\033[96mBZ",  # Belize - Cyan
        '314': "\033[92mBB",  # Barbados - Green
        '321': "\033[94mCR",  # Costa Rica - Blue
        '323': "\033[93mCU",  # Cuba - Yellow
        '327': "\033[95mDM",  # Dominican Republic - Purple
        '329': "\033[96mGP",  # Guadeloupe - Cyan
        '330': "\033[96mGD",  # Grenada - Cyan
        '331': "\033[96mGL",  # Greenland - Cyan
        '332': "\033[96mGT",  # Guatemala - Cyan
        '334': "\033[96mHN",  # Honduras - Cyan
        '336': "\033[96mJM",  # Jamaica - Cyan
        '345': "\033[96mMX",  # Mexico - Cyan
        '347': "\033[96mMQ",  # Martinique - Cyan
        '348': "\033[96mMS",  # Montserrat - Cyan
        '350': "\033[96mNI",  # Nicaragua - Cyan
        '351': "\033[95mPM",  # Panama - Purple
        '352': "\033[95mPM",  # Panama - Purple
        '353': "\033[95mPM",  # Panama - Purple
        '354': "\033[95mPM",  # Panama - Purple
        '355': "\033[95mPM",  # Panama - Purple
        '356': "\033[95mPM",  # Panama - Purple
        '357': "\033[95mPM",  # Panama - Purple
        '358': "\033[95mPR",  # Puerto Rico - Purple
        '359': "\033[95mSV",  # El Salvador - Purple
        '361': "\033[95mTT",  # Trinidad & Tobago - Purple
        '362': "\033[95mTC",  # Turks & Caicos - Purple
        '364': "\033[95mUY",  # Uruguay - Purple
        '365': "\033[95mVC",  # St. Vincent - Purple
        '370': "\033[95mPM",  # Panama - Purple
        '371': "\033[95mPM",  # Panama - Purple
        '372': "\033[95mPM",  # Panama - Purple
        '373': "\033[95mPM",  # Panama - Purple
        '374': "\033[95mPM",  # Panama - Purple

        # South America
        '701': "\033[92mAR",  # Argentina - Green
        '710': "\033[92mBR",  # Brazil - Green
        '720': "\033[92mBO",  # Bolivia - Green
        '725': "\033[94mCL",  # Chile - Blue
        '730': "\033[94mCO",  # Colombia - Blue
        '735': "\033[93mEC",  # Ecuador - Yellow
        '740': "\033[93mFK",  # Falkland Islands - Yellow
        '745': "\033[96mGF",  # French Guiana - Cyan
        '750': "\033[96mGY",  # Guyana - Cyan
        '755': "\033[95mPY",  # Paraguay - Purple
        '760': "\033[95mPE",  # Peru - Purple
        '765': "\033[91mSR",  # Suriname - Red
        '770': "\033[91mUY",  # Uruguay - Red
        '775': "\033[92mVE",  # Venezuela - Green

        # Asia
        '416': "\033[91mTW",  # Taiwan - Red
        '431': "\033[91mJP",  # Japan - Red
        '432': "\033[91mJP",  # Japan - Red
        '440': "\033[91mKR",  # South Korea - Red
        '441': "\033[91mKR",  # South Korea - Red
        '445': "\033[91mKP",  # North Korea - Red
        '412': "\033[93mCH",  # China - Yellow
        '413': "\033[93mCH",  # China - Yellow
        '414': "\033[93mCH",  # China - Yellow
        '417': "\033[93mCH",  # China - Yellow
        '419': "\033[93mIN",  # India - Yellow
        '422': "\033[93mIN",  # India - Yellow
        '423': "\033[93mAZ",  # Azerbaijan - Yellow
        '424': "\033[93mAM",  # Armenia - Yellow
        '425': "\033[93mIQ",  # Iraq - Yellow
        '426': "\033[93mBH",  # Bahrain - Yellow
        '427': "\033[93mBN",  # Brunei - Yellow
        '428': "\033[93mBT",  # Bhutan - Yellow
        '453': "\033[93mHK",  # Hong Kong - Yellow
        '477': "\033[93mHK",  # Hong Kong - Yellow
        '511': "\033[93mPW",  # Palau - Yellow
        '514': "\033[93mKH",  # Cambodia - Yellow
        '515': "\033[93mKH",  # Cambodia - Yellow
        '516': "\033[93mAU",  # Australia - Yellow
        '518': "\033[93mNZ",  # New Zealand - Yellow
        '520': "\033[93mSB",  # Solomon Islands - Yellow
        '525': "\033[93mID",  # Indonesia - Yellow
        '529': "\033[93mID",  # Indonesia - Yellow
        '533': "\033[93mMY",  # Malaysia - Yellow
        '538': "\033[93mMY",  # Malaysia - Yellow
        '548': "\033[93mPH",  # Philippines - Yellow
        '553': "\033[93mPG",  # Papua New Guinea - Yellow
        '555': "\033[93mPN",  # Pitcairn Islands - Yellow
        '557': "\033[93mSB",  # Solomon Islands - Yellow
        '559': "\033[93mTO",  # Tonga - Yellow
        '561': "\033[93mTV",  # Tuvalu - Yellow
        '563': "\033[93mSG",  # Singapore - Yellow
        '564': "\033[93mSG",  # Singapore - Yellow
        '565': "\033[93mSG",  # Singapore - Yellow
        '566': "\033[93mSG",  # Singapore - Yellow
        '567': "\033[93mTH",  # Thailand - Yellow
        '574': "\033[93mVN",  # Vietnam - Yellow
        '576': "\033[93mVU",  # Vanuatu - Yellow
        '577': "\033[93mVU",  # Vanuatu - Yellow
        '578': "\033[93mWF",  # Wallis & Futuna - Yellow
        '601': "\033[93mZA",  # South Africa - Yellow

        # Africa
        '603': "\033[92mAO",  # Angola - Green
        '605': "\033[92mDZ",  # Algeria - Green
        '607': "\033[92mKM",  # Comoros - Green
        '608': "\033[92mCV",  # Cape Verde - Green
        '610': "\033[92mEH",  # Western Sahara - Green
        '611': "\033[92mER",  # Eritrea - Green
        '612': "\033[92mET",  # Ethiopia - Green
        '613': "\033[92mGA",  # Gabon - Green
        '615': "\033[92mGH",  # Ghana - Green
        '616': "\033[92mGM",  # Gambia - Green
        '617': "\033[92mGN",  # Guinea - Green
        '618': "\033[92mGQ",  # Equatorial Guinea - Green
        '619': "\033[92mCI",  # Ivory Coast - Green
        '620': "\033[92mKE",  # Kenya - Green
        '621': "\033[92mLB",  # Liberia - Green
        '622': "\033[92mEG",  # Egypt - Green
        '624': "\033[92mET",  # Ethiopia - Green
        '625': "\033[92mCV",  # Cape Verde - Green
        '626': "\033[92mGA",  # Gabon - Green
        '627': "\033[92mGH",  # Ghana - Green
        '628': "\033[92mGM",  # Gambia - Green
        '629': "\033[92mGN",  # Guinea - Green
        '630': "\033[92mGW",  # Guinea-Bissau - Green
        '631': "\033[92mCI",  # Ivory Coast - Green
        '632': "\033[92mKE",  # Kenya - Green
        '633': "\033[92mBF",  # Burkina Faso - Green
        '634': "\033[92mBI",  # Burundi - Green
        '635': "\033[92mBJ",  # Benin - Green
        '636': "\033[92mLR",  # Liberia - Green
        '637': "\033[92mLR",  # Liberia - Green
        '638': "\033[92mSS",  # South Sudan - Green
        '639': "\033[92mSD",  # Sudan - Green
        '640': "\033[92mST",  # Sao Tome - Green
        '641': "\033[92mSL",  # Sierra Leone - Green
        '642': "\033[92mSN",  # Senegal - Green
        '643': "\033[92mSO",  # Somalia - Green
        '644': "\033[92mSR",  # Suriname - Green
        '645': "\033[92mSZ",  # Swaziland - Green
        '646': "\033[92mTD",  # Chad - Green
        '647': "\033[92mTG",  # Togo - Green
        '648': "\033[92mTN",  # Tunisia - Green
        '649': "\033[92mML",  # Mali - Green
        '650': "\033[92mMZ",  # Mozambique - Green
        '651': "\033[92mMR",  # Mauritania - Green
        '652': "\033[92mMU",  # Mauritius - Green
        '653': "\033[92mMW",  # Malawi - Green
        '654': "\033[92mNE",  # Niger - Green
        '655': "\033[92mNG",  # Nigeria - Green
        '656': "\033[92mNA",  # Namibia - Green
        '657': "\033[92mNC",  # New Caledonia - Green
        '658': "\033[92mNE",  # Niger - Green
        '659': "\033[92mNG",  # Nigeria - Green
        '660': "\033[92mNA",  # Namibia - Green
        '661': "\033[92mRW",  # Rwanda - Green
        '662': "\033[92mSD",  # Sudan - Green
        '663': "\033[92mSN",  # Senegal - Green
        '664': "\033[92mSO",  # Somalia - Green
        '665': "\033[92mST",  # Sao Tome - Green
        '666': "\033[92mSY",  # Syria - Green
        '667': "\033[92mSL",  # Sierra Leone - Green
        '668': "\033[92mSN",  # Senegal - Green
        '669': "\033[92mSO",  # Somalia - Green
        '670': "\033[92mST",  # Sao Tome - Green
        '671': "\033[92mSY",  # Syria - Green
        '672': "\033[92mTD",  # Chad - Green
        '673': "\033[92mTG",  # Togo - Green
        '674': "\033[92mTN",  # Tunisia - Green
        '675': "\033[92mTZ",  # Tanzania - Green
        '676': "\033[92mUG",  # Uganda - Green
        '677': "\033[92mTZ",  # Tanzania - Green
        '678': "\033[92mZM",  # Zambia - Green
        '679': "\033[92mZW",  # Zimbabwe - Green
    }