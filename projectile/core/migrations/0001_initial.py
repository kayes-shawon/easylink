# Generated by Django 2.0.4 on 2018-04-07 11:55

import common.fields
import core.mixins
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('alias', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('status', models.IntegerField(choices=[(1, 'ACTIVE'), (2, 'DRAFT'), (3, 'INACTIVE'), (4, 'REMOVED'), (5, 'DENIED')], default=1)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('username', models.CharField(db_index=True, max_length=30, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('country', models.CharField(choices=[('af', 'Afghanistan\t '), ('al', 'Albania'), ('dz', 'Algeria'), ('as', 'American Samoa'), ('ad', 'Andorra'), ('ao', 'Angola'), ('ai', 'Anguilla'), ('aq', 'Antarctica'), ('ag', 'Antigua and Barbuda'), ('ar', 'Argentina'), ('am', 'Armenia'), ('aw', 'Aruba'), ('ac', 'Ascension Island'), ('au', 'Australia'), ('at', 'Austria'), ('az', 'Azerbaijan'), ('bs', 'Bahamas'), ('bh', 'Bahrain'), ('bd', 'Bangladesh'), ('bb', 'Barbados'), ('by', 'Belarus'), ('be', 'Belgium'), ('bz', 'Belize'), ('bj', 'Benin'), ('bm', 'Bermuda'), ('bt', 'Bhutan'), ('bo', 'Bolivia'), ('ba', 'Bosnia and Herzegovina'), ('bw', 'Botswana'), ('bv', 'Bouvet Island'), ('br', 'Brazil'), ('io', 'British Indian Ocean Territory'), ('vg', 'British Virgin Islands'), ('bn', 'Brunei Darussalam'), ('bg', 'Bulgaria'), ('bf', 'Burkina Faso'), ('bi', 'Burundi'), ('kh', 'Cambodia (Khmer)'), ('cm', 'Cameroon'), ('ca', 'Canada'), ('cv', 'Cape Verde'), ('ky', 'Cayman Islands'), ('cf', 'Central African Republic'), ('td', 'Chad'), ('cl', 'Chile'), ('cx', 'Christmas Island'), ('cc', 'Cocos (Keeling) Islands'), ('co', 'Colombia'), ('km', 'Comoros'), ('ck', 'Cook Islands'), ('cr', 'Costa Rica'), ('hr', 'Croatia (Hrvatska)'), ('cu', 'Cuba'), ('cy', 'Cyprus'), ('cz', 'Czech Republic'), ('ci', "Côte d'Ivoire"), ('cd', 'Democratic Republic of the Congo (Formerly Zaire)'), ('dk', 'Denmark'), ('dj', 'Djibouti'), ('dm', 'Dominica'), ('do', 'Dominican Republic'), ('tp', 'East Timor'), ('ec', 'Ecuador'), ('eg', 'Egypt'), ('sv', 'El Salvador'), ('gq', 'Equatorial Guinea'), ('er', 'Eritrea'), ('ee', 'Estonia'), ('et', 'Ethiopia'), ('eu', 'European Union'), ('fk', 'Falkland Islands'), ('fo', 'Faroe Islands'), ('fm', 'Federated States of Micronesia'), ('fj', 'Fiji'), ('fi', 'Finland'), ('fr', 'France'), ('gf', 'French Guiana'), ('pF', 'French Polynesia With Clipperton Island'), ('tf', 'French Southern and Antarctic Lands'), ('ga', 'Gabon'), ('ge', 'Georgia'), ('de', 'Germany (Deutschland)'), ('gh', 'Ghana'), ('gi', 'Gibraltar'), ('gr', 'Greece'), ('gl', 'Greenland'), ('gd', 'Grenada'), ('gp', 'Guadeloupe'), ('gu', 'Guam'), ('gt', 'Guatemala'), ('gg', 'Guernsey'), ('gn', 'Guinea'), ('gw', 'Guinea-Bissau'), ('gy', 'Guyana'), ('ht', 'Haiti'), ('hm', 'Heard Island and McDonald Islands'), ('hn', 'Honduras'), ('hk', 'Hong Kong'), ('hu', 'Hungary'), ('is', 'Iceland'), ('in', 'India'), ('id', 'Indonesia'), ('ir', 'Iran'), ('iq', 'Iraq'), ('ie', 'Ireland'), ('im', 'Isle of Man'), ('il', 'Israel'), ('it', 'Italy'), ('jm', 'Jamaica'), ('jp', 'Japan'), ('je', 'Jersey'), ('jo', 'Jordan'), ('kz', 'Kazakhstan'), ('ke', 'Kenya'), ('ki', 'Kiribati'), ('kw', 'Kuwait'), ('kg', 'Kyrgyzstan'), ('la', 'Laos'), ('lv', 'Latvia'), ('lb', 'Lebanon'), ('ls', 'Lesotho'), ('lr', 'Liberia'), ('ly', 'Libya'), ('li', 'Liechtenstein'), ('lt', 'Lithuania'), ('lu', 'Luxembourg'), ('mo', 'Macau'), ('mg', 'Madagascar'), ('mW', 'Malawi'), ('my', 'Malaysia'), ('mv', 'Maldives'), ('ml', 'Mali'), ('mt', 'Malta'), ('mh', 'Marshall Islands'), ('mq', 'Martinique'), ('mr', 'Mauritania'), ('mu', 'Mauritius'), ('yt', 'Mayotte'), ('mx', 'Mexico'), ('md', 'Moldova'), ('mc', 'Monaco'), ('mn', 'Mongolia'), ('me', 'Montenegro'), ('ms', 'Montserrat'), ('ma', 'Morocco'), ('mz', 'Mozambique'), ('mm', 'Myanmar'), ('na', 'Namibia'), ('nr', 'Nauru'), ('np', 'Nepal'), ('nl', 'Netherlands'), ('an', 'Netherlands Antilles'), ('nc', 'New Caledonia'), ('nz', 'New Zealand'), ('ni', 'Nicaragua'), ('ne', 'Niger'), ('ng', 'Nigeria'), ('nu', 'Niue'), ('nF', 'Norfolk Island'), ('mp', 'Northern Mariana Islands'), ('no', 'Norway'), ('om', 'Oman'), ('pk', 'Pakistan'), ('pw', 'Palau'), ('ps', 'Palestinian territories\tie, West Bank and Gaza Strip'), ('pa', 'Panama'), ('pg', 'Papua New Guinea'), ('py', 'Paraguay'), ('cn', "People's Republic of China"), ('pe', 'Peru'), ('ph', 'Philippines'), ('pn', 'Pitcairn Islands'), ('pl', 'Poland'), ('pt', 'Portugal'), ('pr', 'Puerto Rico'), ('qa', 'Qatar'), ('mk', 'Republic of Macedonia'), ('cg', 'Republic of the Congo'), ('ro', 'Romania'), ('ru', 'Russia'), ('rw', 'Rwanda'), ('re', 'Réunion'), ('sh', 'Saint Helena'), ('kn', 'Saint Kitts and Nevis'), ('lc', 'Saint Lucia'), ('vc', 'Saint Vincent and the Grenadines'), ('pm', 'Saint-Pierre and Miquelon'), ('ws', 'Samoa (Formerly Western Samoa)'), ('sm', 'San Marino'), ('sa', 'Saudi Arabia'), ('sn', 'Senegal'), ('rs', 'Serbia'), ('sc', 'Seychelles'), ('sl', 'Sierra Leone'), ('sg', 'Singapore'), ('sk', 'Slovakia'), ('si', 'Slovenia'), ('sb', 'Solomon Islands'), ('so', 'Somalia'), ('za', 'South Africa'), ('gs', 'South Georgia and the South Sandwich Islands'), ('kr', 'South Korea'), ('su', 'Soviet Union'), ('es', 'Spain (España)'), ('lk', 'Sri Lanka'), ('sd', 'Sudan'), ('sr', 'Suriname'), ('sj', 'Svalbard and Jan Mayen Islands'), ('sz', 'Swaziland'), ('se', 'Sweden'), ('ch', 'Switzerland'), ('sy', 'Syria'), ('st', 'São Tomé and Príncipe'), ('tw', 'Taiwan'), ('tj', 'Tajikistan'), ('tz', 'Tanzania'), ('th', 'Thailand'), ('gm', 'The Gambia'), ('tl', 'Timor-Leste'), ('tg', 'Togo'), ('tk', 'Tokelau'), ('to', 'Tonga'), ('tt', 'Trinidad and Tobago'), ('tn', 'Tunisia'), ('tr', 'Turkey'), ('tm', 'Turkmenistan'), ('tc', 'Turks and Caicos Islands'), ('tv', 'Tuvalu'), ('vi', 'US Virgin Islands'), ('ug', 'Uganda'), ('ua', 'Ukraine'), ('ae', 'United Arab Emirates'), ('gb', 'United Kingdom'), ('uk', 'United Kingdom'), ('um', 'United States Minor Outlying Islands'), ('us', 'United States of America'), ('uy', 'Uruguay'), ('uz', 'Uzbekistan'), ('vu', 'Vanuatu'), ('va', 'Vatican City State'), ('ve', 'Venezuela'), ('vn', 'Vietnam'), ('wf', 'Wallis and Futuna'), ('ye', 'Yemen'), ('yu', 'Yugoslavia'), ('zm', 'Zambia'), ('zw', 'Zimbabwe')], db_index=True, max_length=2)),
                ('language', models.CharField(default='en', max_length=2)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'TRANSSEXUAL'), (4, 'ANY')], default=1)),
                ('email_on_new_message', models.BooleanField(default=True)),
                ('email_on_new_like', models.BooleanField(default=True)),
                ('email_when_edit_link', models.BooleanField(default=True)),
                ('email_when_edit_category', models.BooleanField(default=True)),
                ('has_newsletter', models.BooleanField(default=True)),
                ('has_weekletter', models.BooleanField(default=True)),
                ('profile_image', common.fields.TimestampImageField(blank=True, null=True, upload_to='profiles/cover')),
                ('hero_image', common.fields.TimestampImageField(blank=True, null=True, upload_to='profiles/avatar')),
                ('entry_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_person_entry_by', to=settings.AUTH_USER_MODEL, verbose_name='entry by')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('updated_by', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='core_person_updated_by', to=settings.AUTH_USER_MODEL, verbose_name='last updated by')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'persons',
            },
            bases=(models.Model, core.mixins.UserThumbFieldMixin),
        ),
    ]
