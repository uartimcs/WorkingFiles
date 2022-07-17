elements_dict = {'H': 'Hydrogen', 'He': 'Helium', 'Li': 'Lithium', 'Be':'Beryllium', 'B': 'Boron',
                    'C': 'Carbon', 'N': 'Nitrogen', 'O': 'Oxygen', 'F':'Fluorine', 'Ne': 'Neon',
                    'Na': 'Sodium', 'Mg': 'Magnesium', 'Al': 'Aluminum', 'Si': 'Silicon', 'P': 'Phosphorus',
                    'S': 'Sulphur', 'Cl': 'Chlorine', 'Ar': 'Argon', 'K': 'Potassium', 'Ca': 'Calcium',
                    'Sc': 'Scandium', 'Ti': 'Titanium','V': 'Vanadium', 'Cr': 'Chromium', 'Mn': 'Manganese',
                    'Fe': 'Iron', 'Co': 'Cobalt', 'Ni': 'Nickel', 'Cu': 'Copper', 'Zn': 'Zinc',
                    'Ga':'Gallium', 'Ge': 'Germanium', 'As': 'Arsenic', 'Se': 'Selenium', 'Br': 'Bromine', 
                    'Kr': 'Krypton', 'Rb': 'Rubidium', 'Sr': 'Strontium', 'Y': 'Yttrium', 'Zr': 'Zirconium',
                    'Nb': 'Niobium', 'Mo': 'Molybdenum', 'Tc': 'Technetium', 'Ru': 'Ruthenium', 'Rh': 'Rhodium',
                    'Pd': 'Palladium', 'Ag': 'Silver', 'Cd': 'Cadmium', 'In': 'Indium', 'Sn': 'Tin',
                    'Sb': 'Antimony', 'Te': 'Tellurium', 'I': 'Iodine', 'Xe': 'Xenon', 'Cs': 'Caesium',
                    'Ba': 'Barium', 'La': 'Lanthanum', 'Ce': 'Cerium', 'Pr': 'Praseodymium', 'Nd': 'Neodymium',
                    'Pm': 'Promethium', 'Sm': 'Samarium', 'Eu': 'Europium', 'Gd': 'Gadolinium', 'Tb': 'Terbium',
                    'Dy':'Dysprosium', 'Ho':'Holmium', 'Er':'Erbium', 'Tm':'Thulium', 'Yb':'Ytterbium',
                    'Lu':'Lutetium', 'Hf':'Hafnium', 'Ta':'Tantalum', 'W':'Tungsten', 'Re':'Rhenium',
                    'Os':'Osmium', 'Ir':'Iridium', 'Pt':'Platinum', 'Au':'Gold', 'Hg':'Mercury',
                    'Tl':'Thallium', 'Pb':'Lead', 'Bi':'Bismuth', 'Po':'Polonium', 'At':'Astatine',
                    'Rn':'Radon', 'Fr':'Francium', 'Ra':'Radium', 'Ac':'Actinium', 'Th':'Thorium',
                    'Pa':'Protactinium', 'U':'Uranium', 'Np':'Neptunium', 'Pu':'Plutonium', 'Am':'Americium',
                    'Cm':'Curium','Bk':'Berkelium','Cf':'Californium','Es':'Einsteinium','Fm':'Fermium',
                    'Md':'Mendelevium','No':'Nobelium','Lr':'Lawrencium','Rf':'Rutherfordium','Db':'Dubuium',
                    'Sg':'Seaborgium','Bh':'Bohrium','Hs':'Hassium','Mt':'Meitnerium','Ds':'Darmstadium',
                    'Rg':'Roentgenium','Cn':'Copernicium','Nh':'Nihonium','Fl':'Flerovium','Mc':'Moscovium',
                    'Lv':'Livermorium','Ts':'Tennessine','Og':'Oganesson'}

status = True
while status:
    ask_query = input("Query for chemical formula [0] or chemical name [1]: ")
    try:
        ask_query = int(ask_query)

        if ask_query not in [0, 1]:
            print("Please enter correct query number. Thanks. ")
            continue

        if ask_query == 1:
            formula = input("Please enter the chemical formula of the element: ")

            if formula in elements_dict:
                print(f"The chemical name of {formula} is {elements_dict[formula]}.")
            else:
                print('This is not a valid name')
        
        elif ask_query == 0:
            name = input("Please enter the chemical name of the elements: ")
            counter = 0

            for i in elements_dict:
                if elements_dict.get(i).lower() == name.lower():
                    print(i)
                    counter += 1
                    break


            if counter == 0:
                print("This is not a valid formula")


        
        search_continue = input("Continue to search: [y/n]: ")
        if search_continue.lower() ==  'y':
            status = True
        elif search_continue.lower() == 'n':
            print("Thanks for using our service. See you next time! ")
            status = False

    except ValueError:
        print('Please enter valid numbers')
    
