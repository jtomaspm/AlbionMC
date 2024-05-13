import { AllItems } from '../screens/items/all';
import { CreateItems } from '../screens/items/create';
import { AllCrafting } from '../screens/crafting/all';
import { CreateCrafting } from '../screens/crafting/create';
import { AllPrices } from '../screens/prices/all';
import { CreatePrices } from '../screens/prices/create';
import { AllSources } from '../screens/sources/all';
import { CreateSources } from '../screens/sources/create';
import Profile from '../screens/profile';
import Settings from '../screens/settings';
import { JSX } from 'solid-js';
import Error from '../screens/error';

export const screens: { [key: string]: JSX.Element } = {
    'error':  <Error />,
    'profile': <Profile />,
    'settings': <Settings />,
    'items/all': <AllItems />,
    'items/create': <CreateItems />,
    'crafting/all': <AllCrafting />,
    'crafting/create': <CreateCrafting />,
    'prices/all': <AllPrices />,
    'prices/create': <CreatePrices />,
    'sources/all': <AllSources />,
    'sources/create': <CreateSources />,
};