{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df65c70a-8598-41de-b9cd-a73588ae9011",
   "metadata": {},
   "outputs": [],
   "source": [
    "def checkIfNotNumeric(*args):\n",
    "    retVal = True\n",
    "    for x in args:\n",
    "        if not(isinstance(x,(int,float))):\n",
    "            return False\n",
    "    return True\n",
    "\n",
    "\n",
    "def addAllNumerics(*args):\n",
    "    s = 0\n",
    "    for x in args:\n",
    "        s += x\n",
    "    return s\n",
    "\n",
    "myName = \"Python Course\""
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
