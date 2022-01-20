{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31ffb24c-bc40-4927-8616-57e93c36a481",
   "metadata": {},
   "outputs": [],
   "source": [
    "import my_module\n",
    "import pandas as pd\n",
    "\n",
    "def test_invocation():\n",
    "    features, target = my_module.get_features_and_target(\n",
    "        csv_file='../data/adult-census.csv',\n",
    "        target_col='class'\n",
    "    )\n",
    "    \n",
    "def test_return_types():\n",
    "    features, target = my_module.get_features_and_target(\n",
    "        csv_file='../data/adult-census.csv',\n",
    "        target_col='class'\n",
    "    )\n",
    "    assert isinstance(features, pd.DataFrame)\n",
    "    assert isinstance(target, pd.Series)\n",
    "    \n",
    "def test_features_dont_contain_target():\n",
    "    features, target = my_module.get_features_and_target(\n",
    "        csv_file='../data/adult-census.csv',\n",
    "        target_col='class'\n",
    "    )\n",
    "    assert target.name not in features.columns"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
