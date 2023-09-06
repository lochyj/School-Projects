import requests
name = input("Enter a planet: ").lower()
api_url = 'https://api.api-ninjas.com/v1/planets?name={}'.format(name)
response = requests.get(api_url, headers={'X-Api-Key': 'V9Kp3Z0+03kgYgKOhOd9tA==jOpiHVovzCKhA9tI'})
if response.status_code == requests.codes.ok:
    print(response)

    rsp = response.text

    print(f"Name: {rsp.name}")
    print(f"Mass: {rsp.mass}")
    print(f"radius: {rsp.radius}")
    print(f"period: {rsp.period}")
    print(f"semi_major_axis: {rsp.semi_major_axis}")
    print(f"temperature: {rsp.temperature}")
    print(f"distance_light_year: {rsp.distance_light_year}")
    print(f"host_star_mass: {rsp.host_star_mass}")
    print(f"host_star_temperature: {rsp.host_star_temperature}")


else:
    print("Error:", response.status_code, response.text)