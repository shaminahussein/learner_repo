<?php

    class Pet{
        //attributes
        var $id;
        var $name;
        var $race;
        var $breed;
        var $gender;

        //methods
        public function set_Pet($id,$name,$race,$breed,$gender){
            $this->id = $id; // '$this' keyword refers to the current object.
            $this->name = $name;
            $this->race = $race;
            $this->breed = $breed;
            $this->gender = $gender;
        }

        public function getValue($item){
            echo $this->$item;
        }

        public function display(){
            echo '<div style="width:30vw; background-color:red; color:white; height:1.3em; font-size:1.5em; padding1em; margin:1em">';

            echo $this->getValue('name');
            echo ' :: ';
            echo $this->getValue('gender');
            echo ' :: ';
            echo $this->getValue('race');
            echo ' :: ';
            echo $this->getValue('breed');

            echo '</div>';
        }
    }

?>