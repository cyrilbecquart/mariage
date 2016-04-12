function compte_a_rebours()
{
	var compte_a_rebours = document.getElementById("compte_a_rebours");

	var date_actuelle = new Date();
	var date_evenement = new Date("Aug 27 13:30:00 2016");
	var total_secondes = (date_evenement - date_actuelle) / 1000;

	var prefixe = "";
	if (total_secondes < 0)
	{
		prefixe = "Ils sont mariés ! <br/>"; // On modifie le préfixe si la différence est négatif
		total_secondes = Math.abs(total_secondes); // On ne garde que la valeur absolue
	}

	if (total_secondes > 0)
	{
		var jours = Math.floor(total_secondes / (60 * 60 * 24));
		var heures = Math.floor((total_secondes - (jours * 60 * 60 * 24)) / (60 * 60));
		minutes = Math.floor((total_secondes - ((jours * 60 * 60 * 24 + heures * 60 * 60))) / 60);
		secondes = Math.floor(total_secondes - ((jours * 60 * 60 * 24 + heures * 60 * 60 + minutes * 60)));

		var mot_jour = "jours";
		var mot_heure = "heures";
		var mot_minute = "minutes";
		var mot_seconde = "secondes";

		if (jours == 1)
		{
			mot_jour = "jour";
		}

		if (heures == 1)
		{
			mot_heure = "heure";
		}

		if (minutes == 1)
		{
			mot_minute = "minute";
		}

		if (secondes == 1)
		{
			mot_seconde = "seconde";
		}


		compte_a_rebours.innerHTML = prefixe + '<span>' + jours + '<br/><span class="cd-word">' + mot_jour + '</span></span><span>' + heures + '<br/><span class="cd-word">' + mot_heure + '</span></span><span>' + minutes + '<br/><span class="cd-word">' + mot_minute + '</span></span><span>' + secondes + '<br/><span class="cd-word">' + mot_seconde + '</span></span>';
	}
	else
	{
		compte_a_rebours.innerHTML = "Rdv à l'église";
	}

	var actualisation = setTimeout("compte_a_rebours();", 1000);
}